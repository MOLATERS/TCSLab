import random
import math
import time
import numpy as np
import scipy.stats as stats


class Item:
    def __init__(self, id, val):
        self.id = id
        self.val = val

    def __str__(self):
        return f"[id: {self.id}, length: {self.length}, line_no: {self.line_no}]"


class SampleBucket:
    def __init__(self, id, start_id, end_id, sample_size, total_size, min_val, max_val):
        self.id = id
        self.start_id = start_id
        self.end_id = end_id
        self.sample_size = sample_size
        self.total_size = total_size
        self.min_val = min_val
        self.max_val = max_val

    def get_scale_factor(self):
        return self.total_size / self.sample_size

    def __str__(self):
        return f"[start_id: {self.start_id}, end_id: {self.end_id}, sample_size: {self.sample_size}, total_size: {self.total_size}, min: {self.min_val}, max: {self.max_val}]"


class SampleItem:
    def __init__(self, original_id, length, line_no, scale_factor=1.0, sample_bucket_id=None):
        self.id = None
        self.original_id = original_id
        self.length = length
        self.line_no = line_no
        self.scale_factor = scale_factor
        self.sample_bucket_id = sample_bucket_id

    def __str__(self):
        return f"[id: {self.id}, length: {self.length}, lineNo: {self.line_no}, scaleFactor: {self.scale_factor}]"


class DatabaseUtil:
    sample_bucket_table = []
    sample_item_table = []
    sorted_item_table = []

    # 创建 样本桶表
    @staticmethod
    def create_sample_bucket_table():
        DatabaseUtil.sample_bucket_table = []

    # 向 样本桶表 中插入样本桶
    @staticmethod
    def insert_sample_bucket(sb):
        DatabaseUtil.sample_bucket_table.append(sb)

    # 从 样本桶 中获取下一个 样本桶
    @staticmethod
    def get_next_sample_bucket(current_id):
        for sb in DatabaseUtil.sample_bucket_table:
            if sb.id > current_id:
                return sb
        return None

    # 创建一个 样本条目表
    @staticmethod
    def create_sample_item_table():
        DatabaseUtil.sample_item_table = []

    # 向 样本条目表 中插入条目
    @staticmethod
    def insert_sample_item(item):
        DatabaseUtil.sample_item_table.append(item)

    # 从 被选择条目表 中获取下一个有效数据
    @staticmethod
    def get_next_valid_item(current_item):
        # 遍历 sorted_item_table 列表，根据条件返回符合要求的数据
        for item in DatabaseUtil.sorted_item_table:
            if item.id > (current_item.id if current_item else 0):
                return item
        return None

    # 从 被选择条目表 中获取指定 id 的数据
    @staticmethod
    def get_item(item_id):
        # 遍历 sorted_item_table 列表，根据条件返回符合要求的数据
        for item in DatabaseUtil.sorted_item_table:
            if item.id == item_id:
                return item
        return None


class Utils:
    # 错误界限和置信水平
    ERROR_BOUND = 60  # 1%
    CONFIDENCE = 0.95

    # 根据输入大小和样本桶计算新的样本大小
    @staticmethod
    def get_new_sample_size(input_size, bucket):
        if input_size == bucket.min_val or input_size == bucket.max_val:
            print("直接返回了，input:", input, "new_sample_size:", bucket.sample_size)
            return bucket.sample_size

        new_sample_size = int(((max(input_size, bucket.max_val) - min(input_size, bucket.min_val)) ** 2) *
                              (math.log(2 / (1 - Utils.CONFIDENCE)) / (2 * (Utils.ERROR_BOUND ** 2))))
        if new_sample_size < 0:
            print("出现负数，", int((max(input_size, bucket.max_val) - min(input_size, bucket.min_val)) ** 2))
        new_sample_size = min(new_sample_size, bucket.end_id - bucket.start_id + 2)
        print("没直接返回，input:", input, "new_sample_size:", new_sample_size)
        return new_sample_size

    # 从样本桶中获取样本ID集合
    @staticmethod
    def get_sample_ids_from_sample_bucket(bucket):
        generated = set()
        while len(generated) < bucket.sample_size:
            next_id = random.randint(bucket.start_Id, bucket.end_Id)
            generated.add(next_id)
        return generated


def calculate_sample_size(error_bound, confidence):
    z_score = stats.norm.ppf(1 - (1 - confidence) / 2)  # Z 分布的分位数
    sample_size = ((z_score ** 2) / (error_bound ** 2)) * 0.25
    return math.ceil(sample_size)


def main():
    TOTAL = 5000  # 数据集大小
    TOTAL = 11
    s = 1.2  # Zipf 分布的参数，控制数据的稀疏程度
    # data = np.random.zipf(s, TOTAL)   # 生成原始数据
    data = np.array([1, 1, 1, 1, 1, 10000, 10000, 10000, 10001, 20000, 21000])
    start_time = time.time()
    data.sort()
    # 创建一个样本桶表
    DatabaseUtil.create_sample_bucket_table()
    # 初始化第一个样本桶，放入第一个数据
    current_sb = SampleBucket(1, 0, 0, 1, TOTAL, data[0], data[0])
    i = 1
    # 对于每个数据，将数据转换为样本条目，计算样本桶的大小
    for item_id in range(1, TOTAL):
        current_item = Item(item_id, data[item_id])
        new_size = Utils.get_new_sample_size(current_item.val, current_sb)

        if current_sb.sample_size + 1 <= new_size:
            current_sb.sample_size = new_size
            current_sb.max_val = max(current_item.val, current_sb.max_val)
            current_sb.min_val = min(current_item.val, current_sb.min_val)
            current_sb.end_id = current_item.id
        else:
            DatabaseUtil.insert_sample_bucket(current_sb)
            i = i + 1
            current_sb = SampleBucket(i, item_id, item_id, 1, TOTAL, data[item_id], data[item_id])
    DatabaseUtil.insert_sample_bucket(current_sb)
    end_time = time.time()
    print("处理时间：", end_time - start_time)
    print("总桶数：", len(DatabaseUtil.sample_bucket_table))
    print("第一个桶的内容：", DatabaseUtil.sample_bucket_table[0])
    print("第二个桶的内容：", DatabaseUtil.sample_bucket_table[1])
    print("最后一个桶的内容：", DatabaseUtil.sample_bucket_table[len(DatabaseUtil.sample_bucket_table) - 1])


if __name__ == "__main__":
    main()

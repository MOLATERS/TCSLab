import time

import numpy as np

from functions.DataType import Element


# 每个矩阵的单位元素
class MatrixElement(Element):
    def __init__(self, index, value):
        super().__init__(value)
        self.index = index

    def __str__(self):
        return "[{}]".format(self.index) + f"{self.value}"

    def __eq__(self, other):
        return self.value == other


# 单一哈希函数
class HashFunction:
    def __init__(self, set_num, data_num):
        self.data_num = data_num
        self.hash_table = np.array([i for i in range(data_num)])
        self.matrix = [MatrixElement(i, 0) for i in range(set_num)]
        time.sleep(0.01)
        np.random.shuffle(self.hash_table)

    def __str__(self):
        phrase = f"\n the hash table is: {self.hash_table}"
        return str(phrase)

    def get_label(self, set_array):
        if set_array is None:
            return -1
        label = float("inf")
        for i in self.hash_table:
            if set_array[i].value == 1:
                return set_array[i].index
        if label != float("inf"):
            return int(label)


#  所有的hash函数集对象
class Hash:
    def __init__(self, hash_num, set_load, data_load):
        self.set_matrix = set_load
        self.data_matrix = data_load
        self.size = hash_num
        self.hash_group = []
        for i in range(hash_num):
            self.hash_group.append(HashFunction(len(set_load), len(data_load)))

    def __str__(self):
        phrase = "the hash size is %d" % self.size
        for x in self.hash_group:
            phrase += str(x) + "\n"
        return phrase

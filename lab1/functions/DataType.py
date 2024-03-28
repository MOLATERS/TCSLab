
# 代表集合元素
class Element:
    def __init__(self, num):
        self.value = num
        self.next = None

    def __str__(self):
        return "the value is: " + str(self.value)

# 代表一个集合对象
class Set(object):
    def __init__(self, index):
        self.index = index
        self.head = None
        self.current = None
        self.matrix = None

    def __str__(self):
        if self.head is None:
            return "Empty List"
        else:
            if self.head.next is None:
                return f"the length of the list is {self.head.value}"
            phrase = ("""The total length is %d 
            """) % self.head.value
            current = self.head.next
            while current.next is not None:
                phrase += "%d->" % current.value
                current = current.next
            return str(phrase + f"{current.value}")

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert(self, item):
        if self.head is None:
            self.head = Element(1)
            self.head.next = Element(item)
            self.current = self.head.next
            return True
        self.current = self.head
        while self.current.next is not None:
            if self.current.next.value == item:
                return False
            self.current = self.current.next
        self.current.next = Element(item)
        self.head.value += 1
        return True


# 代表一个数据集的对象
class DataSet:
    def __init__(self, set_num):
        self.set_group = [Set(i) for i in range(set_num + 1)]
        self.size = set_num

    def __str__(self):
        phrase = f"The data set has {self.size} sets"
        for i in range(self.size):
            phrase += f"{str(self.set_group[i])}\n"
        return phrase

    def insert(self, new_set):
        if self.size < len(self.set_group) - 1:
            self.set_group[self.size - 1] = new_set
            self.set_group[self.size - 1].index = self.size - 1
            self.size += 1
            return True
        self.set_group.append(new_set)
        self.size += 1
        return True


# 代表使用hash函数进行模拟的列表对象方法
class SimList:
    def __init__(self, hash_handler):
        self.hash_handler = hash_handler
        self.size = self.hash_handler.size

    def find_sim(self, index, c):
        count = 0
        good_sim = []
        for i in range(1, len(self.hash_handler.set_matrix)):
            if i <= index:
                continue
            for h in self.hash_handler.hash_group:
                if h.matrix[i - 1] == h.matrix[index - 1] and index != i:
                    count += 1
            sim = float(count / self.hash_handler.size)
            if sim > c:
                good_sim.append([index, i, sim])
            count = 0
        return good_sim

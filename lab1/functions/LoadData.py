import pandas as pd

from functions.DataType import DataSet, Element
from functions.Hash import MatrixElement


def load_data():
    items = pd.read_csv('data/mydata.txt', names=['SetNum', 'Value'], sep="\t")
    datasize = len(items)
    set_num = len(items["SetNum"].drop_duplicates())
    handler = DataSet(set_num)
    set_load = []
    set_count = 1
    data_count = 0
    data_load = []
    for i in range(datasize):
        set_index = items["SetNum"][i]
        value = items["Value"][i]
        try:
            if handler.set_group[set_index].head is not None:
                pass
            else:
                if handler.set_group[0].head is None:
                    handler.set_group[0].head = Element(1)
                else:
                    handler.set_group[0].head.value += 1
            handler.set_group[set_index].index = set_index
            handler.set_group[set_index].insert(value)
            if set_index not in set_load:
                set_load.append(MatrixElement(set_count, set_index))
                set_count += 1
            if value not in data_load:
                data_load.append(MatrixElement(data_count, value))
                data_count += 1
        except IndexError as e:
            print("[error] occurs at:", set_index, value, i)
            break
    return handler, set_load, data_load


def get_matrix(data_handler, index, data_matrix):
    matrix = [MatrixElement(i, 0) for i in range(len(data_matrix))]
    head = data_handler.set_group[index].head.next
    while head:
        for i in range(len(data_matrix)):
            if data_matrix[i].value == head.value:
                matrix[i].value = 1
                break
        head = head.next
    return matrix

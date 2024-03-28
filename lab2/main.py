from lazyselect import lazy_select
from linear import linear
from naive import naive
import numpy as np
import time as t

DATASIZE = 200000
k = 32

def data_generate(name, size):
    if name == "uniform":
        return np.random.uniform(1, 10000, size).astype(int).tolist()
    if name == "normal":
        return np.random.normal(10000, 5000, size).astype(int).tolist()
    if name == "zipf":
        return np.random.zipf(1.2, size).astype(int).tolist()

def main():
    names = ["uniform", "normal", "zipf"]
    good_names = ["uniform", "normal"]
    print("the dataset is", DATASIZE)
    for name in good_names:
        dataset = data_generate(name, DATASIZE)
        print(f"==============the {name} dataset test begin===============")
        naive_begin = t.time()
        result = naive(dataset, k)
        naive_end = t.time()
        print("naive time:", naive_end - naive_begin, "the result is", result)
        linear_begin = t.time()
        result = linear(dataset, 0, len(dataset) - 1, k)
        linear_end = t.time()
        print("linear time:", linear_end - linear_begin, "the result is", result)
        lazy_begin = t.time()
        result = lazy_select(dataset, k, name, 0.9)
        lazy_end = t.time()
        print("lazy select time:", lazy_end - lazy_begin, "the result is", result[name], " for ", result[name+" rounds"], " rounds")

if __name__ == "__main__":
    main()
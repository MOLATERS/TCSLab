from Import import *


def compare():
    data1 = np.load("./output/naive.npy")
    data2 = np.load("./output/minHash.npy")
    count = 0
    for d1 in data1:
        for d2 in data2:
            if d1[0] == d2[0] and d1[1] == d2[1]:
                count += 1
    # print(count / len(data1))
    return count / len(data1)


if __name__ == "__main__":
    compare()

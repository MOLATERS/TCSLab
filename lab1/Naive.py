from Import import *


def intersection(set1, set2):
    head_1 = set1.head.next
    head_2 = set2.head.next
    count = 0
    while head_1:
        while head_2:
            if head_1.value == head_2.value:
                count += 1
                break
            head_2 = head_2.next
        head_1 = head_1.next
    return float(count)


def union(set1, set2):
    head_1 = set1.head.next
    head_2 = set2.head.next
    inter_list = []
    while head_1:
        inter_list.append(head_1.value)
        head_1 = head_1.next
    while head_2:
        if head_2.value not in inter_list:
            inter_list.append(head_2.value)
        head_2 = head_2.next
    return float(len(inter_list))


def naive(c, data_handler):
    # print(data_handler)
    # print("all data loaded ...")
    answer = []
    for x in data_handler.set_group:
        if x.head.next is None:
            continue
        for y in data_handler.set_group:
            if y.head.next is None or y.index <= x.index:
                continue
            sim = intersection(x, y) / union(x, y)
            if sim > c:
                answer.append([x.index, y.index, round(sim, 2)])
    # print(answer)
    np.save("./output/naive.npy", np.array(answer))


if __name__ == '__main__':
    data_handler, _, _ = load_data()
    naive(0.2, data_handler)

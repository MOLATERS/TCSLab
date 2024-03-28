def mergesort(target):
    if len(target) <= 1:
        return target
    mid = len(target) // 2
    left = mergesort(target[:mid])
    right = mergesort(target[mid:])
    return merge(left, right)

def merge(list1, list2):
    i, j = 0, 0
    merge_result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merge_result.append(list1[i])
            i += 1
        else:
            merge_result.append(list2[j])
            j += 1
    merge_result += list1[i:]
    merge_result += list2[j:]
    return merge_result


def naive(target, k):
    target = mergesort(target)
    return target[k-1]

if __name__ == '__main__':
    k = [2, 3, 4, 1, 2, 34, 45, 123, 21, 3, 2, 43, 23, 4, 32324, 4, 32, 34, 6, 7, 56, 8, 0]
    j = [2,3,4,5,6,3,4,5,62]
    # print(merge(k,j))
    print(naive(k,1))
    print(k)
    k = mergesort(k)
    print(k)
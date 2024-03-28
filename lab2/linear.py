from naive import mergesort

def swap(l, a, b):
    if l[a] == l[b]:
        return
    else:
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
    return


def linear(target, left, right, k):
    mid = find_mid(target, left, right)
    i = divide(target, left, right, mid)
    if i - left + 1 == k:
        return target[i]
    elif i - left + 1 > k:
        return linear(target, left, i, k)
    else:
        return linear(target, i + 1, right, k - i + left - 1)


def find_mid(target, left, right):
    if left == right:
        return left
    pointer = left
    # temp = []
    while pointer <= right - 4:
        target[pointer:pointer + 5] = mergesort(target[pointer:pointer + 5])
        # temp.append(target[pointer+2])
        swap(target, pointer + 2, left + (pointer - left) // 5)  # 表示将当前的中位数移动到前面部分
        pointer += 5
    set_num = (pointer - left) // 5
    if right - pointer >= 0:
        set_num += 1
        target[pointer:right + 1] = mergesort(target[pointer:right + 1])
        swap(target, (pointer + right) // 2, left + (pointer - left) // 5)
        # temp.append(target[pointer + (right-pointer)//2])
    if set_num == left:
        return left
    return find_mid(target, left, left + set_num - 1)

# 类似于快排的思路，通过中位数来讲整个数据集分布成两个部分，使用交替替换的策略执行
def divide(target, left, right, mid):
    swap(target, left, mid)
    i = left
    j = right
    x = target[mid]
    while i < j:
        while target[j] >= x and i < j:
            j -= 1
        target[i] = target[j]
        while target[i] < x and i < j:
            i += 1
        target[j] = target[i]
    target[i] = x
    return i


if __name__ == '__main__':
    k = [2, 3, 4, 1, 2, 34, 45, 123, 21, 3, 2, 43, 23, 4, 32324, 4, 32, 34, 6, 7, 56, 8, 0]
    print(linear(k, 0, len(k) - 1, 1))
    print(k)

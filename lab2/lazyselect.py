import numpy as np
from naive import mergesort
import math

def random_sample(data):
    return np.random.choice(data, int(pow(len(data),0.75)), replace=True).tolist()


def get_rank(data, num):
    if num in data:
        count = 1
        for x in data:
            if x < num:
                count += 1
        return count
    return -1


def lazy_select(data, k, name, value):
    result = {}
    round = 0
    sample_size = len(data)
    while True:
        round += 1

        samples = random_sample(data)
        samples = mergesort(samples)

        x = int(k * pow(sample_size, value-1))
        left = max(0, int(x - pow(sample_size, 0.5)))
        right = min(int(pow(sample_size, value)), int(x + math.sqrt(sample_size)))

        l_side = samples[max(1, left - 1)]
        r_side = samples[right - 1]
        l_rank = get_rank(data, l_side)
        r_rank = get_rank(data, r_side)

        valuable = []
        for num in data:
            if l_side <= num <= r_side:
                valuable.append(num)

        if l_rank <= k <= r_rank and len(valuable) <= int(4 * pow(sample_size, value)) + 1:
            valuable = mergesort(valuable)
            result[name] = valuable[k - l_rank]
            result[name + " rounds"] = round 
            break

    return result


if __name__ == '__main__':
    k = [2, 3, 4, 1, 2, 34, 45, 123, 21, 3, 2, 43, 23, 4, 32324, 4, 32, 34, 6, 7, 56, 8, 0]
    print(lazy_select(k, 1, "int", 0.75))

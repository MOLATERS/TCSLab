from Import import *
from Naive import naive
from minHash import minhash
from Compare import compare
import matplotlib.pyplot as plt


def main(data_handler, set_loaded, data_loaded):
    answer = []
    for i in np.arange(0.1, 1, 0.3):
        for j in np.arange(10, 500, 30):
            minhash(j, i, data_handler, set_loaded, data_loaded)
            naive(i, data_handler)
            comp = compare()
            answer.append((round(i, 2), j, comp))
            # print((i, j, comp))
    return answer


def plot_results(results):
    # 分离c值、hash_num和比较结果
    c_values, h_nums, compare_values = zip(*results)

    # 绘制图形
    plt.scatter(h_nums, compare_values, c=c_values, s=5)
    plt.xlabel('Hash Number')
    plt.ylabel('Compare Result')
    unique_c_values = set(c_values)
    for c in unique_c_values:
        indices = [i for i, val in enumerate(c_values) if val == c]
        plt.plot([h_nums[i] for i in indices], [compare_values[i] for i in indices], label=f'c={c}')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    data_handler, set_loaded, data_loaded = load_data()
    print("all data loaded ...")
    plot_results(main(data_handler, set_loaded, data_loaded))

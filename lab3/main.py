from graph import Graph
from timeit import default_timer as timer


def main():

    time_list = []
    weight_list = []
    n_list = [16, 32, 64, 128, 256, 512]
    times_list = [100000, 10000, 1000, 100, 50, 20]

    for j in range(1000):
        weights = 0
        tic = timer()
        for i in range(len(n_list)):
            graph = Graph(n_list[i])
            weight = graph.prim()
            weights += weight
        toc = timer()
        weight_list.append(weights / times_list[i])
        time_list.append((toc - tic) / times_list[i])
    print(weight_list)
    print(time_list)


if __name__ == "__main__":
    main()

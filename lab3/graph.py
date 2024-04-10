import numpy as np

epsilon = 1e-10
INT_MAX = 100


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = np.zeros((n, n))
        for i in range(n):
            for j in range(i, self.n):
                if i == j:
                    self.graph[i][j] = INT_MAX
                else:
                    self.graph[i][j] = np.random.uniform(0+epsilon, 1)
                    self.graph[j][i] = self.graph[i][j]

    def prim(self):
        low = np.zeros(self.n)
        close = np.zeros(self.n, dtype=int)

        k, weight = 0, 0
        for i in range(1, self.n):
            low[i] = self.graph[0][i]
            close[i] = 0

        for i in range(1, self.n):
            min = INT_MAX
            for j in range(1, self.n):
                if low[j] < min:
                    min = low[j]
                    k = j
            weight += min

            low[k] = INT_MAX - 1
            for j in range(1, self.n):
                if self.graph[k][j] < low[j] and abs(low[j] - INT_MAX + 1) > 0.001:
                    low[j] = self.graph[k][j]
                    close[j] = k

        return weight


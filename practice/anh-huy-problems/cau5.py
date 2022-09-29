import numpy as np


class RandomMatrix:
    def __init__(self, min_val=-10, max_val=10, N=4, M=4):
        self.X = np.array([
            np.random.uniform(low=min_val+0.5, high=max_val, size=M)
            for _ in range(N)
        ])

    def set_x_by_csv(self, path):
        with open(path, 'r') as fr:
            res = []

            for line in fr:
                res.append(list(map(float, line.strip().split(','))))

        self.X = np.array(res)

    def save_x_to_csv(self, path):
        string = '\n'.join(
            ','.join(map(str, lst))
            for lst in self.X
        )

        with open(path, 'w') as fw:
            fw.write(string + '\n')

    def update(self, K, alpha=0.1):
        self.X -= alpha * K


mx = RandomMatrix()
print(mx.X)

mx1 = RandomMatrix(min_val=-100, max_val=100)
K = mx1.X

mx.update(K)
print(mx.X)

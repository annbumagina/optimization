import numpy as np

"""
    A - коэффициенты уравнений
    b_x - базисные переменные
    b_v - значение базисных переменных в порядке b_x
    c - коэфиценты функции, которую нужно максимизировать
    f - целевая функция
"""


class SimplexTable:
    def __init__(self, A, b_x, b_v, c):
        self.A = A
        self.b_x = b_x
        self.b_v = b_v
        self.f = c.copy() * (-1)

    # получить текущее решение
    def get_solution(self):
        solution = np.zeros(len(self.A[0]), dtype=float)
        for i in range(len(self.b_v)):
            solution[self.b_x[i]] = self.b_v[i]

        return solution

    # одна итерация симплекс таблицы. Возвращает False, если оптимальное решение уже было достигнуто; True - иначе
    def do_iteration(self):
        column_idx = np.argmin(self.f)
        if self.f[column_idx] >= 0:
            return False

        m = len(self.A)

        def compute_q(i):
            with np.errstate(divide='ignore'):
                return abs(np.float64(self.b_v[i]) / np.float64(self.A[i][column_idx]))

        Q = np.array([compute_q(i) for i in range(m)])
        row_idx = np.argmin(Q)

        self.b_v[row_idx] = self.b_v[row_idx] / self.A[row_idx][column_idx]
        self.A[row_idx] = self.A[row_idx] / self.A[row_idx][column_idx]
        self.b_x[row_idx] = column_idx

        for i in range(m):
            if i == row_idx:
                continue
            k = self.A[i][column_idx] / self.A[row_idx][column_idx]
            self.A[i] = self.A[i] - self.A[row_idx] * k
            self.b_v[i] = self.b_v[i] - self.b_v[row_idx] * k

        k = self.f[column_idx] / self.A[row_idx][column_idx]
        self.f = self.f - self.A[row_idx] * k
        return True


if __name__ == '__main__':
    A = np.array([
        [2., 3., 6., 1., 0., 0.],
        [4., 2., 4., 0., 1., 0.],
        [4., 6., 8., 0., 0., 1.],
    ])
    b = np.array([240., 200., 160.])
    c = np.array([4., 5., 4., 0., 0., 0.])
    b_x = np.array([3, 4, 5])
    b_v = np.array([240., 200., 160.])

    simplex_table = SimplexTable(A, b_x, b_v, c)
    in_process = True
    while in_process:
        in_process = simplex_table.do_iteration()
    solution = simplex_table.get_solution()
    print("Solution: " + str(solution))
    print("Max value: " + str(np.dot(c, solution)))

import numpy as np

"""
    A - коэффициенты уравнений
    b - результаты уравнений
    c - коэфиценты функции, которую нужно максимизировать
    mode - "max" или "min"
"""


class SimplexMethod:
    def __init__(self, A, b, c, mode, basis):
        self.A = A
        self.b = b
        self.mode = mode
        self.c = c
        self.basis = basis
        self.s_x = np.zeros(len(self.A), dtype=int)
        self.s_v = np.zeros(len(self.A), dtype=float)
        self.f = np.zeros(len(self.A[0]), dtype=float)
        self.compute_f()

    # приводит матрицу к единичной и вычисляет оценки
    def compute_f(self):
        m = len(self.A)
        n = len(self.A[0])

        rows = np.zeros(m, dtype=bool)
        for i in range(n):
            if self.basis[i] == .0:
                continue

            t = -1
            for j in range(m):
                if self.A[j][i] != 0 and not rows[j]:
                    t = j
                    rows[j] = True
                    break
            if t == -1:
                raise Exception('wrong basis')

            self.s_x[t] = i
            self.s_v[t] = self.basis[i]

            self.b[t] = self.b[t] / self.A[t][i]
            self.A[t] = self.A[t] / self.A[t][i]
            for p in range(m):
                if p == t:
                    continue
                k = self.A[p][i] / self.A[t][i]
                self.A[p] = self.A[p] - self.A[t] * k
                self.b[p] = self.b[p] - self.b[t] * k

        for i in range(n):
            summ = 0.0
            for j in range(m):
                summ += self.A[j][i] * self.c[self.s_x[j]]
            self.f[i] = summ - self.c[i]

        self.s_v = self.b

    # получить текущее решение
    def get_solution(self):
        solution = np.zeros(len(self.A[0]), dtype=float)
        for i in range(len(self.s_v)):
            solution[self.s_x[i]] = self.s_v[i]

        return solution

    # одна итерация симплекс таблицы. Возвращает False, если оптимальное решение уже было достигнуто; True - иначе
    def do_iteration(self):
        if self.mode == 'max':
            column_idx = np.argmin(self.f)
            if self.f[column_idx] >= 0:
                return False
        elif self.mode == 'min':
            column_idx = np.argmax(self.f)
            if self.f[column_idx] <= 0:
                return False
        else:
            raise RuntimeError('Unexpected mode. Current mode: ' + str(self.mode))

        m = len(self.A)

        def compute_q(i):
            with np.errstate(divide='ignore'):
                return np.float64(self.s_v[i]) / np.float64(self.A[i][column_idx])

        Q = np.array([compute_q(i) for i in range(m)])
        Q[Q < 0] = np.inf
        row_idx = np.argmin(Q)

        self.s_v[row_idx] = self.s_v[row_idx] / self.A[row_idx][column_idx]
        self.A[row_idx] = self.A[row_idx] / self.A[row_idx][column_idx]
        self.s_x[row_idx] = column_idx

        for i in range(m):
            if i == row_idx:
                continue
            k = self.A[i][column_idx] / self.A[row_idx][column_idx]
            self.A[i] = self.A[i] - self.A[row_idx] * k
            self.s_v[i] = self.s_v[i] - self.s_v[row_idx] * k

        k = self.f[column_idx] / self.A[row_idx][column_idx]
        self.f = self.f - self.A[row_idx] * k
        return True

    def solve(self):
        in_process = True
        while in_process:
            in_process = self.do_iteration()

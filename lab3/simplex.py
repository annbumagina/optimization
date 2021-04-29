import copy

import numpy as np

"""
    A - коэффициенты уравнений
    b - результаты уравнений
    c - коэфиценты функции, которую нужно максимизировать
    mode - "max" или "min"
    comp - compare 0 - eq, 1 - less, -1 - greater
"""


class SimplexMethod:
    def __init__(self, A, b, c, mode, basis, comp=None):
        self.A = A
        self.b = b
        self.mode = mode
        self.c = c
        self.basis = basis

        self.extra = self.make_equality(comp)
        self.s_x = np.zeros(len(self.A), dtype=int)
        self.s_v = np.zeros(len(self.A), dtype=float)
        self.f = np.zeros(len(self.A[0]), dtype=float)

        if len(basis) == 0:
            self.find_basis()
        self.compute_f()

    def make_equality(self, comp):
        new_var = 0
        if comp is not None and len(comp[comp != 0]) != 0:
            new_var = len(comp[comp != 0])
            m = len(self.A)
            n = len(self.A[0])

            A = np.zeros((m, n + new_var))
            c = np.zeros(n + new_var)
            A[:, :n] = self.A
            c[:n] = self.c

            t = 0
            for i in range(m):
                if comp[i] != 0:
                    A[i, n + t] = comp[i]
                    t += 1

            self.A = A
            self.c = c
        return new_var

    def find_basis(self):
        m = len(self.A)
        n = len(self.A[0])

        b = copy.deepcopy(self.b)
        A = np.zeros((m, n + m))
        c = np.zeros(n + m)
        basis = np.zeros(n + m)

        c[n:] = -1.
        basis[n:] = b
        A[:, :n] = self.A
        for i in range(m):
            A[i, n + i] = 1.

        simplex = SimplexMethod(A, b, c, 'max', basis)
        simplex.solve()
        self.basis = simplex.get_solution()[:n]

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

        if self.extra > 0:
            solution = solution[:-self.extra]
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
        Q[Q <= 0] = np.inf
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

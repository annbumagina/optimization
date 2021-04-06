import random
import numpy as np
from prettytable import PrettyTable

from lab1.gradient.gradient import Gradient
from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method

eps = 0.001

k_list = [1.0 * t for t in range(1, 6)]
n_list = [t for t in range(2, 6)]

column_list = list(map(str, k_list))
column_list.insert(0, "n \\ k")
table = PrettyTable(column_list)

for n in n_list:
    print(n)
    row = [n]
    for k in k_list:
        a = [0.0 for _ in range(n)]
        start_point = np.array([100.0 for _ in range(n)])

        a[0] = float(k)
        a[1] = 1.0
        for i in range(2, n):
            a[i] = random.uniform(1.0, float(k))


        def target(x):
            return sum([a[t] * x[t] * x[t] for t in range(n)])


        gradient = Gradient(target, start_point, wrap_method(GoldenSectionMethod), eps, "min")
        gradient.compute()
        row.append(gradient.history.iterations)

    table.add_row(row)

print(table)

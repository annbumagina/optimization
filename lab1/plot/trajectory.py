import pylab as plt
import numpy as np


def makeData(func, x_range):
    xgrid = np.array(np.meshgrid(x_range[0], x_range[1]))
    print(xgrid)

    zgrid = func(xgrid)
    print(zgrid)
    return xgrid, zgrid


all_f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]",
         "lambda x: -1 / (1 + x[0]*x[0] + x[1]*x[1])"]
x_ranges = [[np.arange(-20, 20.05, 0.05), np.arange(-20, 20.05, 0.05)],
            [np.arange(-5, 5.05, 0.05), np.arange(-5, 5.05, 0.05)]]
for i in range(len(all_f)):
    f = all_f[i]

    x, z = makeData(eval(f), x_ranges[i])
    cs = plt.contourf(x[0], x[1], z)
    plt.title(f)
    plt.savefig("../results/trajectory_%s.png" % i)
    plt.close()

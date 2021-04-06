import pylab
import numpy as np

from lab1.gradient.gradient import Gradient
from lab1.methods.dichotomy import DichotomyMethod
from lab1.methods.fibonacci import FibonacciMethod
from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method


def makeData(func, x_range):
    xgrid = np.array(np.meshgrid(x_range[0], x_range[1]))
    zgrid = func(xgrid)
    return xgrid, zgrid


all_f = ["lambda x: x[0]*x[0] + x[1]*x[1]",
         "lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]",
         "lambda x: x[0] * x[0] + 20 * x[1] * x[1]"]
start = [np.array([10., 10.]), np.array([10., 10.]), np.array([10, 10.])]
x_ranges = [[np.arange(-15, 15.05, 0.05), np.arange(-15, 15.05, 0.05)],
            [np.arange(-15, 15.05, 0.05), np.arange(-15, 15.05, 0.05)],
            [np.arange(-15, 15.05, 0.05), np.arange(-15, 15.05, 0.05)]]

method_constructors = [DichotomyMethod, GoldenSectionMethod, FibonacciMethod]
eps = 0.001
for i in range(len(all_f)):
    f = all_f[i]
    print("Compute: ", f)
    for method_constructor in method_constructors:
        compute_result = wrap_method(method_constructor)
        gradient = Gradient(eval(f), start[i], compute_result, eps, "min")
        gradient.compute()
        x, z = makeData(eval(f), x_ranges[i])
        pylab.contourf(x[0], x[1], z)
        x0_history = list(map(lambda t: t[0], gradient.get_points()))
        x1_history = list(map(lambda t: t[1], gradient.get_points()))
        pylab.plot(x0_history, x1_history, '-ko')
        pylab.title(f)
        pylab.savefig("results/trajectory_%s_%s.png" % (method_constructor.name(), i))
        pylab.close()

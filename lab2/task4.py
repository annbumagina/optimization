import pylab
import numpy as np

from lab1.gradient.gradient import Gradient
from lab1.methods.dichotomy import DichotomyMethod
from lab1.methods.fibonacci import FibonacciMethod
from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method
from lab2.conjugate_gradient import FletcherReeves
from lab2.newton import Newton


def makeData(func, x_range):
    xgrid = np.array(np.meshgrid(x_range[0], x_range[1]))
    zgrid = func(xgrid)
    return xgrid, zgrid


all_f = ["lambda x: 100 * (x[1] - x[0])**2 + (1 - x[0])**2",
         "lambda x: 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2"]
f_titles = ["f(x,y) = 100 * (y - x)^2 + (1 - x)^2",
            "f(x, y) = 100 * (y - x^2)^2 + (1 - x)^2"]
start = [np.array([2., 10.]), np.array([-5, -10.])]
x_ranges = [[np.arange(-15, 15.05, 0.05), np.arange(-15, 15.05, 0.05)],
            [np.arange(-15, 15.05, 0.05), np.arange(-15, 30.05, 0.05)]]

methods = [Gradient, FletcherReeves, Newton]
epsilon = 0.00001
for i in range(len(all_f)):
    f = all_f[i]
    print("Compute: ", f)
    for method in methods:
        print("\t" + method.name())
        compute_result = wrap_method(GoldenSectionMethod)
        gradient = method(eval(f), start[i], compute_result, epsilon)
        gradient.compute()
        x, z = makeData(eval(f), x_ranges[i])
        pylab.contourf(x[0], x[1], z)
        x0_history = list(map(lambda t: t[0], gradient.get_points()))
        x1_history = list(map(lambda t: t[1], gradient.get_points()))
        pylab.plot(x0_history, x1_history, '-ko')
        pylab.title(f_titles[i] + "\n" + method.name())
        pylab.savefig("results/trajectory_%s_%s.png" % (method.name(), i))
        pylab.close()

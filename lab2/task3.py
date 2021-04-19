import time

import numpy as np
from memory_profiler import memory_usage

from lab1.gradient.gradient import Gradient
from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method
from lab2.conjugate_gradient import FletcherReeves
from lab2.newton import Newton


methods = [Gradient, FletcherReeves, Newton]
f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]", 'lambda x: (x[1] - x[0]**2)**2 + (1 - x[0])**2']
start = [np.array([10, 10.]), np.array([10, 10.])]
extremum = [np.array([0, -1.]), np.array([1, 1])]
eps = 0.0001


def compare():
    for i in range(len(f)):
        for method in methods:
            compute_result = wrap_method(GoldenSectionMethod)
            gradient = method(eval(f[i]), start[i], compute_result, eps)

            def run_method():
                start = time.time()
                gradient.compute()
                end = time.time()
                print("Time spent: " + str(end - start) + " sec")

            mem_usage = memory_usage(run_method, interval=0.001, max_usage=True)
            acc = np.linalg.norm(gradient.result - extremum[i])
            gradient.history.print_history(method.name(), extremum[i], gradient.result, eps, f[i], acc, mem_usage)
            print()


if __name__ == '__main__':
    compare()

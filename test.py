from math import sin, pi

from method import *


def one_dimension_optimization():
    """
    Tests one dimension methods and prints statistics.

    """
    print("=======================")
    print("    ONE DIMENTIONAL    ")
    print("=======================")
    print()

    f = ["lambda x: x*x-5*x+4", "sin", "lambda x: x*x*x-4*x*x+4*x"]
    extremum = [2.5, -pi / 2, 2]
    a = [-1, -pi, 1]
    b = [10, 0, 10]
    epss = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
    comp = lambda f1, f2: f1 < f2
    methods = [dichotomy, golden_section, fibonacci]

    for i in range(len(f)):
        print("function of interest:", f[i])
        print("eps", "dichotomy", "golden_section", "fibonacci")
        for eps in epss:
            result = [eps]
            for method in methods:
                x, it, calls = method(eval(f[i]), a[i], b[i], eps, comp)
                assert abs(x - extremum[i]) < eps
                result.append((it, calls))
            print(result)
        print()


def gradient_decent_simple():
    """
    Tests gradient decent on simple functions and prints statistics.

    """
    print("=======================")
    print("       GRADIENT        ")
    print("=======================")
    print()

    f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]", "lambda x: -1 / (1 + x[0]*x[0] + x[1]*x[1])"]
    start = [np.array([10, 10.]), np.array([10, -10.])]
    extremum = [np.array([0, -1.]), np.array([0, 0.])]
    methods = [dichotomy, golden_section, fibonacci]
    eps = 0.001
    for i in range(len(f)):
        print("function of interest:", f[i])
        print("dich", "gold", "fib")
        result = []
        for method in methods:
            x, it = gradient_decent(eval(f[i]), start[i], method, eps, "min")
            assert np.linalg.norm(x - extremum[i]) < 5 * eps
            result.append(it)
        print(result)
        print()


one_dimension_optimization()
gradient_decent_simple()

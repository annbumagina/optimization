import numpy as np

from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method
from lab2.conjugate_gradient import FletcherReeves
from lab2.newton import Newton


def conjugate_gradient_test():
    """
    Tests gradient on simple functions and prints statistics
    """
    print("========================")
    print("   CONJUGATE GRADIENT   ")
    print("========================")
    print()

    f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]"]
    start = [np.array([10, 10.]), np.array([10, -10.])]
    extremum = [np.array([0, -1.]), np.array([0, 0.])]
    eps = 0.001
    for i in range(len(f)):
        print("function of interest:", f[i])
        compute_result = wrap_method(GoldenSectionMethod)
        gradient = FletcherReeves(eval(f[i]), start[i], compute_result, eps)
        gradient.compute()
        gradient.history.print_history(GoldenSectionMethod.name(), extremum[i], gradient.result, eps, f[i])
        assert np.linalg.norm(gradient.result - extremum[i]) < eps
        print("\tOk\n")
        print()


def newton_test():
    """
    Tests gradient on simple functions and prints statistics
    """
    print("========================")
    print("         NEWTON         ")
    print("========================")
    print()

    f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]"]
    start = [np.array([10, 10.])]
    extremum = [np.array([0, -1.])]
    eps = 0.001
    for i in range(len(f)):
        print("function of interest:", f[i])
        compute_result = wrap_method(GoldenSectionMethod)
        gradient = Newton(eval(f[i]), start[i], compute_result, eps)
        gradient.compute()
        gradient.history.print_history(Newton.name(), extremum[i], gradient.result, eps, f[i])
        assert np.linalg.norm(gradient.result - extremum[i]) < eps
        print("\tOk\n")
        print()


conjugate_gradient_test()
newton_test()

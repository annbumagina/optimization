from math import pi

import numpy as np
from math import *

from lab1.gradient.gradient import Gradient
from lab1.history.history import *
from lab1.methods.abstract_method import AbstractMethod
from lab1.methods.dichotomy import DichotomyMethod
from lab1.methods.fibonacci import FibonacciMethod
from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method


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
    #epss = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
    epss = [0.1, 0.0001, 0.0000001]
    comp = lambda f1, f2: f1 < f2
    method_constructors = [DichotomyMethod, GoldenSectionMethod, FibonacciMethod]

    for i in range(len(f)):
        print("function of interest:", f[i])
        for constructor in method_constructors:
            print("\tmethod: ", constructor.name())
            for eps in epss:
                method = constructor(eval(f[i]), a[i], b[i], eps, comp)
                method.compute()
                method.history.print_history(constructor.name(), extremum[i], method.result, eps, f[i])
                assert abs(method.result - extremum[i]) < eps
            print("\tOk\n")
        print()


class FixedStepMethod(AbstractMethod):
    def __init__(self, target, left, right, eps, compare):
        super().__init__(target, left, right, eps, compare)
        self.result = 0.1

    @staticmethod
    def name():
        return "fixed step"

    def compute(self):
        self.result /= 2


def gradient_decent_simple():
    """
    Tests gradient decent on simple functions and prints statistics
    """
    print("=======================")
    print("       GRADIENT        ")
    print("=======================")
    print()

    f = ["lambda x: 10 * x[0] * x[0] + x[1] * x[1] + 2 * x[1]", "lambda x: -1 / (1 + x[0]*x[0] + x[1]*x[1])"]
    start = [np.array([10, 10.]), np.array([10, -10.])]
    extremum = [np.array([0, -1.]), np.array([0, 0.])]
    method_constructors = [DichotomyMethod, GoldenSectionMethod, FibonacciMethod]
    eps = 0.001
    for i in range(len(f)):
        print("function of interest:", f[i])
        for method_constructor in method_constructors:
            print("\tmethod: ", method_constructor.name())
            compute_result = wrap_method(method_constructor)
            gradient = Gradient(eval(f[i]), start[i], compute_result, eps)
            gradient.compute()
            gradient.history.print_history(method_constructor.name(), extremum[i], gradient.result, eps, f[i])
            assert np.linalg.norm(gradient.result - extremum[i]) < eps
            print("\tOk\n")
        print()


one_dimension_optimization()
gradient_decent_simple()

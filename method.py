"""
Methods to find extremum of function

Args:
    f    (function): Function to explore.
    a, b    (float): Interval of interest.
    eps     (float): Accuracy of result.
    comp (function): < for min, > for max.
Returns:
    x   (float): Extremum of function.
    it    (int): Number of iterations performed.
    calls (int): Number of function calls performed.

"""
from math import sqrt
import numpy as np
import numdifftools as nd


def dichotomy(f, a, b, eps, comp):
    it = 0
    calls = 0
    while abs(a - b) / 2 > eps:
        it += 1
        calls += 2

        x = (a + b) / 2
        f1 = f(x - eps)
        f2 = f(x + eps)
        if comp(f1, f2):
            b = x
        else:
            a = x

    return (a + b) / 2, it, calls


def golden_section(f, a, b, eps, comp):
    it = 0
    calls = 1

    phi = (1 + sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f(x1)
    f2 = f(x2)
    while abs(a - b) / 2 > eps:
        it += 1
        calls += 1

        if comp(f1, f2):
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - x2)
            if abs(a - b) > eps:
                f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (x1 - a)
            if abs(a - b) > eps:
                f2 = f(x2)

    return (a + b) / 2, it, calls


def fib(max_fib):
    lst = [1, 1]
    while lst[-1] <= max_fib:
        lst.append(lst[-1] + lst[-2])
    return lst, len(lst) - 1


def fibonacci(f, a, b, eps, comp):
    F, n = fib((b - a) / eps)
    it = 0

    x1 = a + (b - a) * F[n-2] / F[n]
    x2 = a + (b - a) * F[n-1] / F[n]
    f1 = f(x1)
    f2 = f(x2)
    for i in range(1, n):
        it += 1

        if comp(f1, f2):
            b = x2
            x2 = x1
            f2 = f1
            if i < n - 1:
                x1 = a + (b - a) * F[n - i - 2] / F[n - i]
                f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            if i < n - 1:
                x2 = a + (b - a) * F[n-i-1] / F[n-i]
                f2 = f(x2)
    return (a + b) / 2, it, n


def gradient_decent(f, x, step_func, eps, extremum):
    fgrad = nd.Gradient(f)
    it = 0
    while True:
        it += 1

        if extremum == "min":
            alpha = step_func(lambda alpha: f(x - alpha * fgrad(x)), 0, 1000, eps, lambda f1, f2: f1 < f2)[0]
            xnew = x - alpha * fgrad(x)
        else:
            alpha = step_func(lambda alpha: f(x + alpha * fgrad(x)), 0, 1000, eps, lambda f1, f2: f1 > f2)[0]
            xnew = x + alpha * fgrad(x)

        if np.linalg.norm(xnew - x) < eps:
            return xnew, it
        x = xnew

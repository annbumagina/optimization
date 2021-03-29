from math import sqrt
import numpy as np
import numdifftools as nd


def dichotomy(f, a, b, eps, comp):
    while abs(a - b) > eps:
        x = (a + b) / 2
        f1 = f(x - eps)
        f2 = f(x + eps)
        if comp(f1, f2):
            b = x
        else:
            a = x
    return (a + b) / 2


def golden_section(f, a, b, eps, comp):
    phi = (1 + sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f(x1)
    f2 = f(x2)
    while abs(a - b) > eps:
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
    return (a + b) / 2


def fib(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst


# todo: make with eps
def fibonacci(f, a, b, n, comp):
    F = fib(n)
    x1 = a + (b - a) * F[n-2] / F[n]
    x2 = a + (b - a) * F[n-1] / F[n]
    f1 = f(x1)
    f2 = f(x2)
    for i in range(1, n - 1):
        if comp(f1, f2):
            b = x2
            x2 = x1
            f2 = f1
            if i < n - 2:
                x1 = a + (b - a) * F[n - i - 2] / F[n - i]
                f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            if i < n - 2:
                x2 = a + (b - a) * F[n-i-1] / F[n-i]
                f2 = f(x2)
    return (a + b) / 2


# todo: can't find max?
def gradient_decent(f, x, step_func, eps):
    fgrad = nd.Gradient(f)
    while True:
        alpha = step_func(lambda alpha: f(x - alpha * fgrad(x)), 0, 10, eps, lambda f1, f2: f1 < f2)
        xnew = x - alpha * fgrad(x)
        if np.linalg.norm(xnew - x) < eps:
            return xnew
        x = xnew


print(golden_section(lambda x: x*x-5*x+4, -1, 10, 0.000001, lambda f1, f2: f1 < f2))
print(fibonacci(lambda x: x*x-5*x+4, -1, 10, 20, lambda f1, f2: f1 < f2))
print(gradient_decent(lambda x: 10*x[0]*x[0]+x[1]*x[1]+2*x[1], np.array([10, 10.]), dichotomy, 0.00001))

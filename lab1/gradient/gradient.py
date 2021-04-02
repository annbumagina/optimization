from typing import Callable
import numpy as np
import numdifftools as nd

from lab1.methods.abstract_method import AbstractMethod


class Gradient:
    def __init__(self,
                 target: Callable,
                 start_point: np.ndarray,
                 method_constructor: Callable,
                 eps: float,
                 extremum_type: str):
        self.target = target
        self.start_point = start_point
        self.method_constructor = method_constructor
        self.eps = eps
        self.extremum_type = extremum_type
        self.it = 0
        self.result = None
        self.history = []

    def compute(self):
        fgrad = nd.Gradient(self.target)
        x = self.start_point
        while True:
            self.it += 1

            if self.extremum_type == "min":
                def optimize(t):
                    return self.target(x - t * fgrad(x))

                method: AbstractMethod = self.method_constructor(optimize, 0, 1000, self.eps, lambda f1, f2: f1 < f2)
                method.compute()
                alpha = method.result
                xnew = x - alpha * fgrad(x)
            else:
                def optimize(t):
                    return self.target(x + t * fgrad(x))

                method: AbstractMethod = self.method_constructor(optimize, 0, 1000, self.eps, lambda f1, f2: f1 > f2)
                method.compute()
                alpha = method.result
                xnew = x + alpha * fgrad(x)

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break
            x = xnew

from typing import Callable
import numpy as np
import numdifftools as nd

from lab1.history.history import GradientHistory


class Gradient:
    def __init__(self,
                 target: Callable,
                 start_point: np.ndarray,
                 optimize_method: Callable,
                 eps: float,
                 extremum_type: str):
        self.target = target
        self.start_point = start_point
        self.optimize_method = optimize_method
        self.eps = eps
        self.extremum_type = extremum_type
        self.it = 0
        self.result = None
        self.history = GradientHistory(['x', 'fgrad', 'alpha'])

    def compute(self):
        fgrad = nd.Gradient(self.target)
        x = self.start_point

        self.history.add_iteration(x, fgrad(x), '-')

        while True:
            if self.extremum_type == "min":
                def for_optimize(t):
                    return self.target(x - t * fgrad(x))

                alpha = self.optimize_method(for_optimize, 0, 1000, self.eps, lambda f1, f2: f1 < f2)
                xnew = x - alpha * fgrad(x)
            else:
                def for_optimize(t):
                    return self.target(x + t * fgrad(x))

                alpha = self.optimize_method(for_optimize, 0, 1000, self.eps, lambda f1, f2: f1 < f2)
                xnew = x + alpha * fgrad(x)

            self.history.add_iteration(xnew, fgrad(x), alpha)

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break
            x = xnew

from typing import Callable
import numpy as np
import numdifftools as nd

from lab1.history.history import GradientHistory


class Gradient:
    def __init__(self,
                 target: Callable,
                 start_point: np.ndarray,
                 optimize_method: Callable,
                 eps: float):
        self.target = target
        self.start_point = start_point
        self.optimize_method = optimize_method
        self.eps = eps
        self.it = 0
        self.result = None
        self.history = GradientHistory(['x', 'fgrad', 'alpha'])

    @staticmethod
    def name():
        return "gradient"

    def compute(self):
        fgrad = nd.Gradient(self.target)
        x = self.start_point

        self.history.add_iteration(x, fgrad(x), '-')

        while True:
            grad_x = fgrad(x)

            def for_optimize(t):
                self.history.op(x.size * 2)
                return self.target(x - t * grad_x)

            alpha = self.optimize_method(for_optimize, 0, 1., self.eps, lambda f1, f2: f1 < f2)
            xnew = x - alpha * grad_x

            self.history.op(x.size * 2)
            self.history.add_iteration(xnew, grad_x, alpha)

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break
            x = xnew

    def get_points(self):
        return self.history.get_column(1)

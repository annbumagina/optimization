from typing import Callable
import numpy as np
import numdifftools as nd

from lab1.history.history import GradientHistory
from lab2.conjugate_gradient import FletcherReeves


class Newton:
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
        self.history = GradientHistory(['x', 'alpha'])

    @staticmethod
    def name():
        return "newton"

    def compute(self):
        H = nd.Hessian(self.target)
        grad = nd.Gradient(self.target)
        x = self.start_point
        self.history.add_iteration(x, '-')

        while True:
            def phi(t):
                return self.target(x) + grad(x).dot(t - x) + 0.5 * H(x).dot(t - x).dot(t - x)

            gradient = FletcherReeves(phi, self.start_point, self.optimize_method, self.eps)
            gradient.compute()
            xt = gradient.result

            def psi(t):
                return self.target(x + t * (xt - x))

            h = self.optimize_method(psi, 0, 1000, self.eps, lambda f1, f2: f1 < f2)
            xnew = x + h * (xt - x)
            self.history.add_iteration(xnew, h)

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break

            x = xnew
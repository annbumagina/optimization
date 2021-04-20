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
            target_x = self.target(x)
            grad_x = grad(x)
            H_x = H(x)

            def phi(t):
                n = x.size
                self.history.op(n)
                u = t - x
                self.history.op(n + 2*n-1 + n + n + n*(2*n-1) + 2*n-1)
                return target_x + grad_x.dot(u) + 0.5 * H_x.dot(u).dot(u)

            gradient = FletcherReeves(phi, self.start_point, self.optimize_method, self.eps, ops=self.history.operations)
            gradient.compute()
            xt = gradient.result

            def psi(t):
                self.history.op(x.size * 3)
                return self.target(x + t * (xt - x))

            h = self.optimize_method(psi, 0, 1., self.eps, lambda f1, f2: f1 < f2)
            xnew = x + h * (xt - x)

            self.history.op(x.size * 2)
            self.history.add_iteration(xnew, h)

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break

            x = xnew

    def get_points(self):
        return self.history.get_column(1)

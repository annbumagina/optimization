from typing import Callable
import numpy as np
import numdifftools as nd

from lab1.history.history import GradientHistory, Operations


class FletcherReeves:
    def __init__(self,
                 target: Callable,
                 start_point: np.ndarray,
                 optimize_method: Callable,
                 eps: float,
                 ops: Operations = None):
        self.target = target
        self.start_point = start_point
        self.optimize_method = optimize_method
        self.eps = eps
        self.it = 0
        self.result = None
        self.history = GradientHistory(['x', 'alpha', 'vector'], ops=ops)

    @staticmethod
    def name():
        return "conjugate gradient"

    def compute(self):
        fgrad = nd.Gradient(self.target)
        x = self.start_point
        fgrad_x = fgrad(x)
        vector = -fgrad_x

        self.history.add_iteration(x, '-', '-')

        while True:
            def for_optimize(t):
                self.history.op(x.size * 2)
                return self.target(x + t * vector)

            alpha = self.optimize_method(for_optimize, 0, 0.1, self.eps, lambda f1, f2: f1 < f2)
            xnew = x + alpha * vector

            self.history.op(x.size * 2)
            self.history.add_iteration(xnew, alpha, np.linalg.norm(vector))

            if np.linalg.norm(xnew - x) < self.eps:
                self.result = xnew
                break

            fgrad_xnew = fgrad(xnew)
            gamma = np.inner(fgrad_xnew, fgrad_xnew) / np.inner(fgrad_x, fgrad_x)
            self.history.op(fgrad_x.size * 4 - 1)
            vector = -fgrad_xnew + gamma * vector
            self.history.op(vector.size * 2)
            fgrad_x = fgrad_xnew
            x = xnew

    def get_points(self):
        return self.history.get_column(1)

"""
Methods to find extremum of function

Args:
    target       (function): Target function to explore.
    left, right  (float): Interval of interest.
    eps          (float): Accuracy of result.
    compare      (function): < for min, > for max.
Results:
    result  (float): Extremum of function.
    it      (int): Number of iterations performed.
    calls   (int): Number of function calls performed.
"""
from typing import Callable


class AbstractMethod:
    def __init__(self, target: Callable, left: float, right: float, eps: float, compare: Callable):
        self.it = 0
        self.calls = 0
        self.target = target
        self.left = left
        self.right = right
        self.eps = eps
        self.compare = compare
        self.result = None

    def compute(self):
        pass

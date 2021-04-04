from math import sqrt

from lab1.methods.abstract_method import AbstractMethod


class GoldenSectionMethod(AbstractMethod):
    def __init__(self, target, left, right, eps, compare, history):
        super().__init__(target, left, right, eps, compare, history)

    @staticmethod
    def name():
        return "golden_section"

    def compute(self):
        self.calls = 1

        a = self.left
        b = self.right

        phi = (1 + sqrt(5)) / 2
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi
        f1 = self.target(x1)
        f2 = self.target(x2)
        while abs(a - b) / 2 > self.eps:
            self.history.add_iteration(1, a, b, x1, x2, f1, f2)

            if self.compare(f1, f2):
                b = x2
                x2 = x1
                f2 = f1
                x1 = a + (b - x2)
                if abs(a - b) > self.eps:
                    f1 = self.target(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = b - (x1 - a)
                if abs(a - b) > self.eps:
                    f2 = self.target(x2)

        self.result = (a + b) / 2

from lab1.methods.abstract_method import AbstractMethod
from lab1.history.history import History


class DichotomyMethod(AbstractMethod):
    def __init__(self, target, left, right, eps, compare):
        super().__init__(target, left, right, eps, compare)

    @staticmethod
    def name():
        return "dichotomy"

    def compute(self):
        a = self.left
        b = self.right
        while abs(a - b) / 2 > self.eps:
            x1 = (a + b) / 2 - self.eps / 3
            x2 = (a + b) / 2 + self.eps / 3
            f1 = self.target(x1)
            f2 = self.target(x2)

            self.history.add_iteration(2,
                                       History.pair_format((a, b)),
                                       History.pair_format((x1, x2)),
                                       History.pair_format((f1, f2)))

            if self.compare(f1, f2):
                b = x2
            else:
                a = x1

        self.result = (a + b) / 2

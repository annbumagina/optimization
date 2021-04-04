from lab1.methods.abstract_method import AbstractMethod


class DichotomyMethod(AbstractMethod):
    def __init__(self, target, left, right, eps, compare, history=None):
        super().__init__(target, left, right, eps, compare, history)

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

            if self.history is not None:
                self.history.add_iteration(2, a, b, x1, x2, f1, f2)

            if self.compare(f1, f2):
                b = x2
            else:
                a = x1

        self.result = (a + b) / 2

from methods.abstract_method import AbstractMethod


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
            self.it += 1
            self.calls += 2

            x1 = (a + b) / 2 - self.eps / 3
            x2 = (a + b) / 2 + self.eps / 3
            f1 = self.target(x1)
            f2 = self.target(x2)
            if self.compare(f1, f2):
                b = x2
            else:
                a = x1

        self.result = (a + b) / 2

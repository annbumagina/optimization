from lab1.methods.abstract_method import AbstractMethod


class FibonacciMethod(AbstractMethod):
    def __init__(self, target, left, right, eps, compare):
        super().__init__(target, left, right, eps, compare)

    @staticmethod
    def name():
        return "fibonacci"

    @staticmethod
    def fib(max_fib):
        lst = [1, 1]
        while lst[-1] <= max_fib:
            lst.append(lst[-1] + lst[-2])
        return lst, len(lst) - 1

    def compute(self):
        a = self.left
        b = self.right
        F, n = self.fib((b - a) / self.eps)

        x1 = a + (b - a) * F[n - 2] / F[n]
        x2 = a + (b - a) * F[n - 1] / F[n]
        f1 = self.target(x1)
        f2 = self.target(x2)

        for i in range(1, n):
            self.history.add_iteration(1, a, b, x1, x2, f1, f2)

            if self.compare(f1, f2):
                b = x2
                x2 = x1
                f2 = f1
                if i < n - 1:
                    x1 = a + (b - a) * F[n - i - 2] / F[n - i]
                    f1 = self.target(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                if i < n - 1:
                    x2 = a + (b - a) * F[n - i - 1] / F[n - i]
                    f2 = self.target(x2)

        self.result = (a + b) / 2

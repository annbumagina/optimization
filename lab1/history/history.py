from prettytable import PrettyTable


class History:
    def __init__(self):
        self.iterations = 0
        self.calls = 0
        self.interval = []
        self.points = []
        self.points_values = []
        self.table = PrettyTable(['Iteration', 'Interval', 'points', 'f(points)'])

    def add_iteration(self, calls: int, left: float, right: float, x1, x2, f1, f2):
        self.iterations = self.iterations + 1
        self.calls = self.calls + calls
        self.interval.append((left, right))
        self.__add_points(x1, x2, f1, f2)

    def __add_points(self, x1, x2, f1, f2):
        self.points.append((x1, x2))
        self.points_values.append((f1, f2))

    def print_history(self, method_name: str, expected, result, eps: float, function: str):
        for i in range(self.iterations):
            self.table.add_row([i,
                                self.interval[i],
                                self.points[i],
                                self.points_values[i]])

        print("Method: " + method_name)
        print("Function: " + function)
        print("Eps: " + str(eps))
        print("Expected: " + str(expected) + "\tResult: " + str(result))
        print("Iterations: " + str(self.iterations))
        print("Calls: " + str(self.calls))
        print(self.table)
        print()

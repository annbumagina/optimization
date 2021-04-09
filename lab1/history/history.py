from prettytable import PrettyTable


class AbstractHistory:
    def __init__(self, columns: list):
        columns.insert(0, 'Iteration')
        self.table = PrettyTable(columns)
        self.size = len(columns)
        self.columns = [[None for y in range(0)] for x in range(len(columns))]

        for c in columns:
            self.table.float_format[c] = ".7"

    def get_column(self, column_index):
        return self.columns[column_index]


class History(AbstractHistory):
    def __init__(self, columns: list):
        super().__init__(columns)
        self.iterations = 0
        self.calls = 0

    def add_iteration(self, calls: int, *args):
        if len(args) + 1 != self.size:
            return "Incorrect number of arguments"
        self.columns[0].append(self.iterations)
        self.iterations = self.iterations + 1
        self.calls = self.calls + calls
        for i in range(len(args)):
            self.columns[i + 1].append(args[i])

    def print_history(self, method_name: str, expected, result, eps: float, function: str):
        for i in range(self.iterations):
            row = []
            for column in self.columns:
                row.append(column[i])
            self.table.add_row(row)

        print("Method: " + method_name)
        print("Function: " + function)
        print("Eps: " + str(eps))
        print("Expected: " + str(expected) + "\tResult: " + str(result))
        print("Iterations: " + str(self.iterations))
        print("Calls: " + str(self.calls))
        print(self.table.get_csv_string(delimiter="\t"))
        print()

    @staticmethod
    def pair_format(pair, signs=7):
        return ("%.7f" % pair[0],
                "%.7f" % pair[1])


class GradientHistory(AbstractHistory):
    def __init__(self, columns):
        super().__init__(columns)
        self.iterations = 0

    def add_iteration(self, *args):
        if len(args) + 1 != self.size:
            return "Incorrect number of arguments"
        self.columns[0].append(self.iterations)
        self.iterations = self.iterations + 1
        for i in range(len(args)):
            self.columns[i + 1].append(args[i])

    def print_history(self, method_name: str, expected, result, eps: float, function: str):
        for i in range(self.iterations):
            row = []
            for column in self.columns:
                row.append(column[i])
            self.table.add_row(row)

        print("Method: " + method_name)
        print("Function: " + function)
        print("Eps: " + str(eps))
        print("Expected: " + str(expected) + "\tResult: " + str(result))
        print("Iterations: " + str(self.iterations))
        print(self.table.get_csv_string(delimiter="\t"))
        print()

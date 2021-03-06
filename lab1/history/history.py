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


class Operations:
    def __init__(self):
        self.operations = 0

    def op(self, cnt):
        self.operations = self.operations + cnt


class GradientHistory(AbstractHistory):
    def __init__(self, columns, ops=None):
        super().__init__(columns)
        self.iterations = 0
        self.operations = Operations()
        if ops is not None:
            self.operations = ops

    def add_iteration(self, *args):
        if len(args) + 1 != self.size:
            return "Incorrect number of arguments"
        self.columns[0].append(self.iterations)
        self.iterations = self.iterations + 1
        for i in range(len(args)):
            self.columns[i + 1].append(args[i])

    def op(self, cnt):
        self.operations.op(cnt)

    def print_history(self, method_name: str, expected, result, eps: float, function: str, acc: float = None):
        for i in range(self.iterations):
            row = []
            for column in self.columns:
                row.append(column[i])
            self.table.add_row(row)

        print("Method: " + method_name)
        print("Function: " + function)
        print("Eps: " + str(eps))
        if acc is not None:
            print("Accuracy: " + str(acc))
        print("Expected: " + str(expected) + "\tResult: " + str(result))
        print("Operations: " + str(self.operations.operations))
        print("Iterations: " + str(self.iterations))
        rows = sum(1 for _ in self.table)
        step = rows // 10 + 1
        print('\n'.join(self.table.get_csv_string(delimiter="\t").splitlines()[::step]))
        print()

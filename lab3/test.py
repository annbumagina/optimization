import numpy as np

from lab3.simplex import SimplexMethod


# Solution: [40.0, 0.0, 0.0, 160.0, 40.0, 0.0]
# Max value: 160.0
def test_0():
    A = np.array([
        [2., 3., 6., 1., 0., 0.],
        [4., 2., 4., 0., 1., 0.],
        [4., 6., 8., 0., 0., 1.],
    ])
    b = np.array([240., 200., 160.])
    c = np.array([4., 5., 4., 0., 0., 0.])

    simplex_table = SimplexMethod(A, b, c, 'max')
    in_process = True
    while in_process:
        in_process = simplex_table.do_iteration()
    solution = simplex_table.get_solution()
    print("Test 0")
    print("Solution: " + str(solution))
    print("Max value: " + str(np.dot(c, solution)))
    print()


# Solution: [0.0, 4.0, 0.0, 0.0]
# Min value: -4.0
def test_1():
    A = np.array([
        [3., 1., -1., 1.],
        [5., 1., 1., -1.]
    ])
    b = np.array([4., 4.])
    c = np.array([-6., -1., -4., 5.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_2():
    A = np.array([
        [1., -3., -1., -2.],
        [1., -1., 1., 0.]
    ])
    b = np.array([-4., 0.])
    c = np.array([-1., -2., -3., 1.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_3():
    A = np.array([
        [1., 1., 0., 2., 1.],
        [1., 1., 1., 3., 2.],
        [0., 1., 1., 2., 1.]
    ])
    b = np.array([5., 9., 6.])
    c = np.array([-1., -2., -3., 3., -1.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_4():
    A = np.array([
        [1., 1., 2., 0., 0.],
        [0., -2., -2., 1., -1.],
        [1., -1., 6., 1., 1.]
    ])
    b = np.array([4., -6., 12.])
    c = np.array([-1., -1., -1., 1., -1.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_5():
    A = np.array([
        [1., 1., -1., -10.],
        [1., 14., 10., -10.]
    ])
    b = np.array([0., 11.])
    c = np.array([-1., 4., -3., 10.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_6():
    A = np.array([
        [1., 3., 3., 1., 1., 0.],
        [2., 0., 3., -1., 0., 1.]
    ])
    b = np.array([3., 4.])
    c = np.array([-1., 5., 1., -1., 0., 0.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def test_7():
    A = np.array([
        [3., 1., 1., 1., -2.],
        [6., 1., 2., 3., -4.],
        [10., 1., 3., 6., -7.]
    ])
    b = np.array([10., 20., 30.])
    c = np.array([-1., -1., 1., -1., 2.])

    print_result(SimplexMethod(A, b, c, 'min'), c)


def print_result(simplex_table, c):
    simplex_table.solve()
    solution = simplex_table.get_solution()
    print("Test 1")
    print("Solution: " + str(solution))
    print("Min value: " + str(np.dot(c, solution)))
    print()


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()

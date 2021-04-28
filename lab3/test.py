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
    basis = np.array([0., 0., 0., 240., 200., 160.])

    simplex = SimplexMethod(A, b, c, 'max', basis)
    print_result(0, simplex, c)


# Solution: [0.0, 4.0, 0.0, 0.0]
# Min value: -4.0
def test_1():
    A = np.array([
        [3., 1., -1., 1.],
        [5., 1., 1., -1.]
    ])
    b = np.array([4., 4.])
    c = np.array([-6., -1., -4., 5.])
    basis = np.array([1., 0., 0., 1.])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(1, simplex, c)


def test_2():
    A = np.array([
        [1., -3., -1., -2.],
        [1., -1., 1., 0.]
    ])
    b = np.array([-4., 0.])
    c = np.array([-1., -2., -3., 1.])
    basis = np.array([0., 1., 1., 0.])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(2, simplex, c)


def test_3():
    A = np.array([
        [1., 1., 0., 2., 1.],
        [1., 1., 1., 3., 2.],
        [0., 1., 1., 2., 1.]
    ])
    b = np.array([5., 9., 6.])
    c = np.array([-1., -2., -3., 3., -1.])
    basis = np.array([0., 0., 1., 2., 1.])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(3, simplex, c)


def test_4():
    A = np.array([
        [1., 1., 2., 0., 0.],
        [0., -2., -2., 1., -1.],
        [1., -1., 6., 1., 1.]
    ])
    b = np.array([4., -6., 12.])
    c = np.array([-1., -1., -1., 1., -1.])
    basis = np.array([1., 1., 2., 0., 0.])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(4, simplex, c)


def test_5():
    A = np.array([
        [1., 1., -1., -10.],
        [1., 14., 10., -10.]
    ])
    b = np.array([0., 11.])
    c = np.array([-1., 4., -3., 10.])
    basis = np.array([])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(5, simplex, c)


def test_6():
    A = np.array([
        [1., 3., 3., 1., 1., 0.],
        [2., 0., 3., -1., 0., 1.]
    ])
    b = np.array([3., 4.])
    c = np.array([-1., 5., 1., -1., 0., 0.])
    basis = np.array([])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(5, simplex, c)


def test_7():
    A = np.array([
        [3., 1., 1., 1., -2.],
        [6., 1., 2., 3., -4.],
        [10., 1., 3., 6., -7.]
    ])
    b = np.array([10., 20., 30.])
    c = np.array([-1., -1., 1., -1., 2.])
    basis = np.array([])

    simplex = SimplexMethod(A, b, c, 'min', basis)
    print_result(5, simplex, c)


def print_result(test_id, simplex_table, c):
    simplex_table.solve()
    solution = simplex_table.get_solution()
    print("Test " + str(test_id))
    print("Solution: " + str(solution))
    print("Min value: " + str(np.dot(c, solution)))
    print()


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    # test_3()
    # test_4()
    # test_5()
    # test_6()
    # test_7()

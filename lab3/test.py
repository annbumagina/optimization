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
    c = np.array([4., 5., 4., 0., 0., 0.])
    b_x = np.array([3, 4, 5])
    b_v = np.array([240., 200., 160.])

    simplex_table = SimplexMethod(A, b_x, b_v, c, 'max')
    in_process = True
    while in_process:
        in_process = simplex_table.do_iteration()
    solution = simplex_table.get_solution()
    print("Test 0")
    print("Solution: " + str(solution))
    print("Max value: " + str(np.dot(c, solution)))
    print()


# Solution: [0.0, 0.0, 0.0, 0.0]
# Min value: 0.0
def test_1():
    A = np.array([
        [3., 1., -1., 1.],
        [5., 1., 1., -1.]
    ])
    c = np.array([-6., -1., -4., 5.])
    b_x = np.array([0, 3])
    b_v = np.array([1., 1.])

    simplex_table = SimplexMethod(A, b_x, b_v, c, 'min')
    simplex_table.solve()
    solution = simplex_table.get_solution()
    print("Test 1")
    print("Solution: " + str(solution))
    print("Min value: " + str(np.dot(c, solution)))
    print()


if __name__ == '__main__':
    test_0()
    test_1()

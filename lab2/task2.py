import numpy as np
import time as time
import multiprocessing

from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method
from lab2.conjugate_gradient import FletcherReeves

box = {
    1: {
        'function': 'lambda x: 100 * (x[1] - x[0])**2 + (1 - x[0])**2',
        'extremum': np.array([1, 1]),
        'starts': [np.array([10, 10]), np.array([-10, -10]), np.array([1, 1]), np.array([123, 65]),
                   np.array([-54, 54])],
    },
    2: {
        'function': 'lambda x: 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2',
        'extremum': np.array([1, 1]),
        'starts': [np.array([1, 1]), np.array([2, 2]), np.array([10, 10]), np.array([0, 0]), np.array([-3, 3])],
    }
}

methods = [GoldenSectionMethod]
# epsilon = 0.0001 fix
epsilon = 0.00001


def _test(function: str, start_pos, extremum, opt_method, eps):
    print("Testing function:", function)
    compute_result = wrap_method(opt_method)
    gradient = FletcherReeves(eval(function), start_pos, compute_result, eps)
    gradient.compute()
    gradient.history.print_history(opt_method.name(), extremum, gradient.result, eps, function)

    if np.linalg.norm(gradient.result - extremum) < eps:
        print("\tTest completed!\n")
    else:
        print("\n\tTest failed! " + "expected: " + str(extremum) + " result: " + str(gradient.result) + " \n")
    print()


if __name__ == '__main__':
    for i in box:
        print()
        print("#########################START##################################")
        print()
        for method in methods:
            print()
            print("Starting test function:" + box[i]["function"] + " with method: " + method.name())
            for start in box[i]["starts"]:
                try:
                    print("Start position: " + str(start))
                    p = multiprocessing.Process(
                        target=_test(box[i]["function"], start, box[i]["extremum"], method, epsilon))
                    p.start()

                    p.join(2)  # 2 seconds

                    if p.is_alive():
                        print("\n\tTime's up!\n")
                        print("Fail compute function: " + box[i]['function'] + " in start: " + str(start))
                        p.terminate()

                    while p.is_alive():
                        pass
                except IndexError:
                    print("\n\tTest failed! Overflow encountered in double_scalars! \n")
                    print("Fail compute function: " + box[i]['function'] + " in start: " + str(start))
                    print()
            print()

        print()
        print("#########################END##################################")

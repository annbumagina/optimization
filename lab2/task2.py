import numpy as np
import time as time
import multiprocessing
import math
from memory_profiler import profile

from lab1.methods.golden_section import GoldenSectionMethod
from lab1.methods.wrapper import wrap_method
from lab2.conjugate_gradient import FletcherReeves
from lab2.newton import  Newton
from lab1.gradient.gradient import Gradient

"""
    Если вайт лист не пустой, то будут считаться функции только из этого листа
"""

white_list = []

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
        'starts': [np.array([1, 1]), np.array([2, 2]), np.array([0, 0]), np.array([-3, 3]),
                   np.array([2, 4]), np.array([1, 0.5])],
    },
    3: {
        'function': 'lambda x: -(2 * math.exp(-((x[0] - 1) / 2)**2 - ((x[1] - 1) / 1)**2) '
                    '+ 3 * math.exp(-((x[0] - 2) / 3)**2 - ((x[1] - 3) / 2)**2))',
        'extremum': np.array([1.2630, 1.33439]),
        'starts': [np.array([0, 0]), np.array([3, 0]), np.array([-1, 0]), np.array([-3, 3]), np.array([1, 1])],
    }
}

methods = [Gradient, FletcherReeves, Newton]
epsilon = 0.00001


#@profile
def _test(method, function: str, start_pos, extremum, eps):
    print("Testing function:", function)
    compute_result = wrap_method(GoldenSectionMethod)
    gradient = method(eval(function), start_pos, compute_result, eps)
    gradient.compute()
    #gradient.history.print_history(method.name(), extremum, gradient.result, eps, function)

    if np.linalg.norm(gradient.result - extremum) < 0.1:
        print("\tTest completed!\n")
    else:
        print("\n\tTest failed! " + "expected: " + str(extremum) + " result: " + str(gradient.result) + " \n")
    print()


if __name__ == '__main__':
    if len(white_list) > 0:
        print("\n\n\tWarning! White list not empty!")

    for i in box:
        if len(white_list) > 0:
            if i not in white_list:
                continue
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
                        target=_test(method, box[i]["function"], start, box[i]["extremum"], epsilon))
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

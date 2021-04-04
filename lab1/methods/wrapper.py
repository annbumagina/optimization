from typing import Callable

from lab1.methods.abstract_method import AbstractMethod


def wrap_method(method_constructor):
    def return_result_function(target, left, right, eps, compare):
        method: AbstractMethod = method_constructor(target, left, right, eps, compare)
        method.compute()
        return method.result

    return return_result_function

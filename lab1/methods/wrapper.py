from typing import Callable

from lab1.methods.abstract_method import AbstractMethod
from lab1.history.history import History

def wrap_method(method_constructor):
    def return_result_function(target, left, right, eps, compare):
        method: AbstractMethod = method_constructor(target, left, right, eps, compare)
        method.compute()
        return method.result

    return return_result_function

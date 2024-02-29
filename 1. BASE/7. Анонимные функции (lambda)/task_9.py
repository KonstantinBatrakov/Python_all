"""Простейшие анонимные функции"""


def named_func(param):
    return param ** 0.5


print(named_func(100))  # -> 10.0

square_rt = lambda param: param ** 0.5
print(square_rt(100))  # -> 10.0

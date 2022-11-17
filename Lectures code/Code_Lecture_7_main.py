
# numbers = [9, 1, 1, 2, 5, 6, 7, 3]
# print(len(numbers))
# count = 0
# for i in range(len(numbers)):
#
#     if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
#         count += 1
#
# print(count)


# def get_max_n  C'


# print(get_max_number(5, 10, 7))
# print(get_max_number(15, 10, 7))
# print(get_max_number(7, 15, 7))


# def foo(number):
#     print(number ** number)
#
#
# def greetings(name):
#     print(f'Hello {name}')
#
# foo(5)

# b = foo(3)
# print('SUM', a + b)
# response = greetings('Petr')
# print('Response value is', response)


# def output_1(result):
#     print('------')
#     print(f'|{str(result).zfill(4)}|')
#     print('------')
#
#
# def output_2(result):
#     print('+____+')
#     print(f'|{str(result).zfill(4)}|')
#     print('+----+')
#
#
# def math_func(a, b, out_func):
#     c = a ** b
#     out_func(c)

# math_func(2, 5, output_1)
# math_func(2, 5, output_2)


# def default_args(a, b=None, c=None):
#     print(f'A = {a} | B = {b} | C = {c}')
#
#
# default_args(b=1, c=2, a=3)
# default_args(1, 3, c=2)
# default_args(1)
# default_args(c=2, a=1)
# def sum_int(a = 4):
#     a += 1
#     print(a)
#
# sum_int(1)
# sum_int()
# sum_int()
# sum_int()

# def list_sum(numbers=None):
#     if numbers is None:
#         numbers = []
#     numbers.append(1)
#     print(sum(numbers))
#
# list_sum([1, 2, 3])
# list_sum()  # 1
# list_sum()  # 1
# list_sum()  # 1
# list_sum()  # 1
# print(1, 2, 3, 4, 5, 6,6 ,6, 6, 6, 6, 6, 6, 6, 6, 6)


# def default_args_v2(*args, **kwargs):
#     print(args, kwargs)
#
#
# default_args_v2(1, 2, 3, 4, 5, 6, 7, 8, 2, 3, var='hello', k={'key': 'val'}, a=777, variable='Hello world')

# x = 15


# def global_view():
#     global x
#
#     x = 30
#     print(f'global_view x = {x}')
#
#
# def local_view():
#     x = 20
#     print(f'local_view x = {x}')

# def nonlocal_view():
#     x = 10
#
#     print(f'1) nonlocal_view x = {x}')
#
#     def inner():
#         nonlocal x
#         x = 5
#         print(f'inner x = {x}')
#
#     inner()
#     print(f'2) nonlocal_view x = {x}')
#
#
# nonlocal_view()

# x = 15
#
# print(f'1) global x = {x}')
# global_view()
# # local_view()
# print(f'2) global x = {x}')

# from typing import Union, Optional
#
#
# AnnotationType = Union[int, float, list]
#
#
# def annotations(a: AnnotationType, b: AnnotationType = 10) -> Optional[AnnotationType]:
#     print(f'A = {a} Type = {type(a)} | B = {b} Type = {type(b)}')
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a * b
#     elif isinstance(a, list) and isinstance(b, list):
#         return a + b
#
#
# test = annotations(4, 2)
# c = 4
# print(isinstance(c, str))
# print(isinstance(c, (float, int)))
# print(type(c) == int)
# print(test, type(test))

# def foo(x: any):
#     return x + 1

# foo = lambda a, b: a + b
#
# print(foo(5, 2))
#
# numbers = [1, 2, 3, 4, -10]
#
# new_numbers = list(map(lambda x: -x, numbers))
# print(new_numbers)

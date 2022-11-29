from typing import List, Union, Tuple
import random

a = 1


# def sum_all(*args: Union[float, int]) -> Union[float, int]:
#     MyVar = 2  # noqa
#     value = 0
#     for num in args:
#         value += num
#     return value
#
# print(sum_all(1, 2, 3.4))


# contacts = [
#     {
#         'name': 'John',
#         'phone': '123456789',
#     },
#     {
#         'name': 'Mary',
#         'phone': '987654321',
#     },
#     {
#         'name': 'Vasya',
#         'phone': '123456789',
#     },
#     {
#         'name': 'Anna',
#         'phone': '987654321',
#     }
# ]
#
# sorted_contacts = sorted(contacts, key=lambda x: x['name'])
# print(sorted_contacts)


# def sum_all_sequences(number: Union[int, float]):
#     print(f'Number = {number}')
#     if number == 10:
#         return number
#     return sum_all_sequences(number + 1)


# print(sum_all_sequences(1))

import time


# def very_slow_function(max_number: int) -> int:
#     result = 0
#     for i in range(max_number):
#         result += i
#     return result
#
#

#
#
# def get_run_time(func, *args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     print(f'func = {func} | time = {time.time() - start}')
#     return result


# print(get_run_time(very_slow_function, 1000000))
# print(get_run_time(very_slow_function, 10000000))
# print(get_run_time(say_hello, 'Petr', 25))
# print(time.time())

# from utils import decorators
# import utils
# print('OUTPUT FROM main.py', decorators.very_slow_function(100))

# import random
#
# print(random.a)

# random.randint()

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# from a import tests as test_from_a
# from b import tests as test_from_b
#
# print(test_from_a.a)
# print(test_from_b.b)


# from utils.additional import *
#
# run_browser()

# decorators.run_browser()
# decorators.test_first_screen()
# print('...')
# ...
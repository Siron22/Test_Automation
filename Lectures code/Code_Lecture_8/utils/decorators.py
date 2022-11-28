import time
import random


from utils.additional import *


say_hello('Petr', 30)


def hello_decorator(func):
    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner


def get_run_time(func):

    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'func = {func} | time = {time.time() - start}')
        return result

    return inner


# print(function_to_be_used('Petr'))
# run_1 = ~get_run_time(function_to_be_used)
# run_2 = run_1('Petr')
# print(run_2)
...
# class HelloDecorator:
#
#     def __call__(self, func):
#         def wrapper():
#             print("[Class HelloDecorator] Hello, this is before function execution")
#             result = func()
#             print("[Class HelloDecorator] This is after function execution")
#             return result
#
#         return wrapper
...


def timeit(filename, tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(f'{func.__name__}[{tag}] {time.time() - start} seconds\n')

            return result

        return wrapper

    return decorator


@timeit('data.log', tag='New Function')
def function_to_be_used(name: str):
    print("This is inside the function !!")
    return f'Hello {name}!'


@timeit('data.log', tag='Old Function')
def very_slow_function(max_number: int) -> int:
    result = 0
    for i in range(max_number):
        result += i
    return result

#
# very_slow_function(20)
# very_slow_function(200000)

# print(__name__)


def go_to_first_screen():
    pass


def test_first_screen():
    pass


if __name__ == '__main__':
    run_browser()
    go_to_first_screen()
    test_first_screen()
    # print('OUTPUT FROM decorators.py', function_to_be_used('Petr'))


...
# class Timeit:
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func(*args, **kwargs)
#
#             with open(self.filename, 'a') as f:
#                 f.write(f'{func.__name__} {time.time() - start} seconds\n')
#
#             return result
#
#         return wrapper
# @Timeit('log.txt')
# def very_slow_function():
#     time.sleep(random.randint(1, 3))
#     print('Very slow function')
...
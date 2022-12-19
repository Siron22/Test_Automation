# import time
#
#
# def hello_decorator(func):
#     def inner():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#
#     return inner
#
#
# def timeit(filename):
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func(*args, **kwargs)
#
#             with open(filename, 'a') as f:
#                 f.write(f'{func.__name__} {time.time() - start} seconds\n')
#
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @hello_decorator
# def function_to_be_used():
#     print("This is inside the function !!")
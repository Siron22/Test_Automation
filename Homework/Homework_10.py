# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'

counter = {}
text = 'Function {} was called {} times.\n'


def call_times(file_name):
    def inner(func):
        def wrapper():
            wrapper.count += 1
            counter[func.__name__] = wrapper.count
            with open(file_name, 'w') as f:
                for func_name, quantity in counter.items():
                    f.write(text.format(func_name, quantity))
            return func()
        wrapper.count = 0
        return wrapper
    return inner


@call_times('deco_test.txt')
def baa():
    pass


@call_times('deco_test.txt')
def daa():
    pass


@call_times('deco_test.txt')
def zaa():
    pass


for i in range(10):
    baa()

for i in range(20):
    daa()

for i in range(100):
    zaa()

print(counter)




# Решение № 2. Записывает количество вызовов для каждой функции в отдельный файл путём перезаписи последней строки.
# не применимо для записи всех результатов в один файл
# def call_times(file_name):
#     def inner(func):
#         def wrapper():
#             wrapper.count += 1
#             with open(file_name, 'w') as f:
#                 f.write(f'Function {func.__name__} was called {wrapper.count} times.\n')
#             return func()
#
#         wrapper.count = 0
#         return wrapper
#
#     return inner
#
#


# l_times('deco_test.txt')
# def baa():
#     pass
#
#
# @call_times('deco_test1.txt')
# def daa():
#     pass
#
#
# @call_times('deco_test2.txt')
# def zaa():
#     pass
#
#
# for i in range(5):
#     baa()
#
# for i in range(7):
#     daa()
#
# for i in range(4):
#     zaa()
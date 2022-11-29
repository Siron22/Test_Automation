# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'


def call_times(file_name):
    def inner(func):
        def wrapper():
            wrapper.count += 1
            with open(file_name, 'a') as f:
                f.write(f'Function {func.__name__} was called {wrapper.count} times.\n')
            return func()

        wrapper.count = 0
        return wrapper

    return inner


count = 0


@call_times('deco_test.txt')
def baa():
    pass


@call_times('deco_test.txt')
def daa():
    pass


@call_times('deco_test.txt')
def zaa():
    pass


for i in range(7):
    baa()

for i in range(8):
    daa()

for i in range(5):
    zaa()

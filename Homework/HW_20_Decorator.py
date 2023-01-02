"""Написать декоратор skip, которым можно декорировать функции.
Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.
Если выражение condition ложное, функция должна выполнится."""


def skip(condition, reason=''):
    def inner(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f'{reason}')
            else:
                return func(*args, **kwargs)
        return wrapper
    return inner


@skip(condition=False, reason='Skipped because of Gladiolus')
def test_func(a, b):
    c = a + b
    return c

@skip(condition=False, reason='Skipped because of Gladiolus')
def foo(number):
    return number ** number

@skip(condition=False, reason='Skipped because of Gladiolus')
def greetings(name):
    return f'Hello {name}'

@skip(condition=False, reason='Skipped because of Gladiolus')
def is_power_of_two(a: int, n=2) -> str:
    if n > a:
        return "NO"
    elif n < a:
        return is_power_of_two(a, n * 2)
    else:
        return "YES"




print(foo(5))
print(greetings('Vasya'))
print(is_power_of_two(255))
print(test_func(2, 3))

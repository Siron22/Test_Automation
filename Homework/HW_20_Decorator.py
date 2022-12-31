"""Написать декоратор skip, которым можно декорировать функции.
Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.
Если выражение condition ложное, функция должна выполнится."""


def skip(condition, reason=''):
    def inner(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f'{reason}')
            else:
                func(*args, **kwargs)
        return wrapper
    return inner


@skip(condition=False, reason='Skipped because of Gladiolus')
def test_func(a, b):
    c = print(a + b)
    return c

@skip(condition=False, reason='Skipped because of Gladiolus')
def foo(number):
    print(number ** number)

@skip(condition=False, reason='Skipped because of Gladiolus')
def greetings(name):
    print(f'Hello {name}')

@skip(condition=False, reason='Skipped because of Gladiolus')
def is_power_of_two(a: int, n=2) -> str:
    if n > a:
        print("NO")
        return "NO"
    elif n < a:
        return is_power_of_two(a, n * 2)
    else:
        print("YES")
        return "YES"




foo(5)
greetings('Vasya')
is_power_of_two(255)
test_func(2, 3)

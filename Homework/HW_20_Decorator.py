"""Написать декоратор skip, которым можно декорировать функции.
Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.
Если выражение condition ложное, функция должна выполнится."""


def skip(condition, reason=''):
    def inner(func):
        def wrapper():
            if condition:
                print(f'{reason}')
            else:
                func()
        return wrapper

    return inner


@skip(condition=5*5==24, reason='Skipped because of Gladiolus')
def test_two_plus_two():
    print("Function completed")

test_two_plus_two()

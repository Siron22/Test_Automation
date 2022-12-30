"""Написать декоратор skip, которым можно декорировать функции.
Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.
Если выражение condition ложное, функция должна выполнится."""

def skip(condition, reason=''):
    pass


@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
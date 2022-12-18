# Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):
# Lecture  1: 17 Oct 2022 19:15
# Lecture  2: 20 Oct 2022 19:15
# ...
# Lecture  9: 14 Nov 2022 19:15
# Lecture 10: 17 Nov 2022 19:15
# ...
# Lecture 32: 02 Feb 2023 19:15

from datetime import *

a = 0
lec_date = datetime(2022, 10, 14, 19, 15)
for _ in range(16):
    a += 1
    t1 = timedelta(days=3)
    t2 = timedelta(days=4)
    lec_date += t1
    lec_format = lec_date.strftime("%d %b %Y %H:%M")
    print(f'Lecture {a}: {lec_format}')
    a += 1
    lec_date += t2
    lec_format = lec_date.strftime("%d %b %Y %H:%M")
    print(f'Lecture {a}: {lec_format}')



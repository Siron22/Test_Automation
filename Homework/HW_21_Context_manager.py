"""
Написать класс Timer для измерения времени выполнения кода.
Прошедшее время должен возвращать в аттрибуте elapsed_time.
Класс должен применяться как контекстный менеджер.
У класса должен быть метод reset.
Если между использованием контекстного менеджера вызывался метод reset, прошедшее время должно считаться заново.
Если метод reset не вызывался, в elapsed_time должно быть сохранено время выполнения всех фрагментов кода обернутых
контекстным менеджером.
"""
import time


class Timer:

    def __init__(self):
        elapsed_time = 0
        start_time = time.time()
        self.start_time = start_time
        self.elapsed_time = elapsed_time

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.time() - self.start_time
        self.start_time += self.elapsed_time
        return self.elapsed_time

    def reset(self):
        self.start_time = time.time()


print(">>>>t:")
with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds
with t:
    time.sleep(3)
print(t.elapsed_time)  # ~6 seconds
with t:
    time.sleep(1)
print(t.elapsed_time)  # ~7 seconds
t.reset()
with t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 seconds
print(">>>>t2:")
with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds

with Timer() as t:
    time.sleep(1)

time.sleep(2)
print(t.elapsed_time)  # ~1 second

with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds expected, but shows ~5
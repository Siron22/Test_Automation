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
    elapsed_time = 0
    start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Timer.elapsed_time = time.time() - Timer.start_time
        return Timer.elapsed_time

    def __next__(self):
        Timer.start_time += Timer.elapsed_time

    def reset(self):
        Timer.start_time = time.time()


# with Timer() as t:
#     time.sleep(1)
# print(t.elapsed_time)  # ~1 second
# with t:
#     time.sleep(2)
# print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds

"""
General conceptions
    Synchronous/asynchronous programming, concurrency/parallelism
    Asynchronous tools in Python
    Peculiarities of multithreading in Python. GIL
    When to use multithreading
Multithreading
    Creating thread
    Passing parameters in to thread
    Daemon-threads
    Joining threads
    Returning value from threads
    Race conditions. Deadlock
    Practical case with server and concurrent writing to file


Useful links:

https://docs.python.org/3/library/threading.html    Thread-based parallelism
https://botfather.dev/blog/async-in-python    Асинхронность в Python
https://docs.python.org/3/library/asyncio.html    Asynchronous I/O

"""

import time
import random

is_first_run = True


def fixture():
    print("Do some preparation...")
    global is_first_run
    if is_first_run:
        for i in range(5):
            time.sleep(1)
            print('.', end='')
        is_first_run = False
    print()


def qtest1():
    fixture()
    print("Test1")


def qtest2():
    fixture()
    print("Test2")


if random.random() < 0.5:
    qtest1()
    qtest2()
else:
    qtest2()
    qtest1()

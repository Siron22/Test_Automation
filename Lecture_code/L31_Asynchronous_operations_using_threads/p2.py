import time
import threading


def do_job1():

    for i in range(5):
        print(f"In child do_job1: {i}")
        time.sleep(0.5)

def do_job2():

    for i in range(5):
        print(f"In child do_job2: {i}")
        time.sleep(0.1)




thread1 = threading.Thread(target=do_job)
thread1.start()

thread2 = threading.Thread(target=do_job2)
thread2.start()

for i in range(4):
    print(f"In main: {i}")
    time.sleep(0.8)
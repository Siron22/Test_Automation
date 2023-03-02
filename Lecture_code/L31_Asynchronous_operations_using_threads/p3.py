import threading
import time


def do_job(message, n, wait):

    for i in range(n):
        print(f"{message}: {i}")
        time.sleep(wait)

# thread1 = threading.Thread(target=do_job, args=('In child do_job1', 5, 0.2))
# thread2 = threading.Thread(target=do_job, args=('In child do_job2', 3, 0.5))

thread1 = threading.Thread(target=do_job, kwargs={'message': 'In child do_job1', 'n': 5, 'wait': 0.2})
thread2 = threading.Thread(target=do_job, kwargs={'message': 'In child do_job2', 'n': 3, 'wait': 0.5})


thread1.start()
thread2.start()


for i in range(4):
    print(f"In main: {i}")
    time.sleep(0.8)

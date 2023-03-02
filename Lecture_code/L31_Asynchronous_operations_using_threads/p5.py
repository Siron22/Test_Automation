import time
import threading


def do_job():

    for i in range(5):
        print(f"In child do_job1: {i}")
        time.sleep(0.6)


thread = threading.Thread(target=do_job, name="QQQ")
thread.start()
print(thread.is_alive())
#thread.join(2)

print(thread.name)

for i in range(5):
    print(f"In main: {i}")
    time.sleep(0.2)

thread.join()
print(thread.is_alive())
import time

def do_job():

    for i in range(5):
        print(f"In main do_job: {i}")
        time.sleep(0.5)

do_job()

for i in range(4):
    print(f"In main: {i}")
    time.sleep(0.8)
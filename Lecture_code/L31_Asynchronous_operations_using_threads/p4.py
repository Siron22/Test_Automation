import time
import threading


# def do_job():
#
#     for i in range(5):
#         print(f"In child do_job1: {i}")
#         time.sleep(0.6)
#
# thread = threading.Thread(target=do_job, daemon=True)
# thread.start()
#
#
# for i in range(5):
#     print(f"In main: {i}")
#     time.sleep(0.2)



# def do_job():
#     i = 0
#     while True:
#         print(f"In child do_job1: {i}")
#         i += 1
#         time.sleep(0.6)
#
# thread = threading.Thread(target=do_job, daemon=True)
# thread.start()
#
#
# for i in range(5):
#     print(f"In main: {i}")
#     time.sleep(0.2)


run = True
def do_job():
    i = 0
    while run:
        print(f"In child do_job1: {i}")
        i += 1
        time.sleep(0.6)

thread = threading.Thread(target=do_job)
thread.start()


for i in range(5):
    print(f"In main: {i}")
    time.sleep(0.2)

time.sleep(2)
run = False
print("END")


class Collector:

    def __init__(self):
        self._thread = threading.Thread(target=self.collect)
        self.collection = []
        self.running = True
        self._thread.start()

    def collect(self):
        while self.running:
            print("Server is running")
            self.collection.append(2)

    def stop_collecting(self):
        self.running = False

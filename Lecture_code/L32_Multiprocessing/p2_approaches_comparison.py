import time
from time import sleep

from threading import Thread
from multiprocessing import Process


def do_io_job():
    print("Start waiting")
    sleep(1)
    print("End waiting")


def do_cpu_job():
    import random
    import math
    lst = [random.random() for i in range(1000_000)]
    sinuses = [math.sin(i) for i in lst]
    powers = [pow(i, 4.454355) for i in lst]


# start_time = time.perf_counter_ns()
# for i in range(5):
#     do_io_job()
# end_time = time.perf_counter_ns()
# print(f"Sync io task performed in {(end_time - start_time)/1000_000}, s")
#
#
# start_time = time.perf_counter_ns()
# threads = []
# for i in range(5):
#     thread = Thread(target=do_io_job)
#     threads.append(thread)
#     thread.start()
# for t in threads:
#     t.join()
# end_time = time.perf_counter_ns()
# print(f"Async io task performed in {(end_time - start_time)/1000_000}, s")
#
# start_time = time.perf_counter_ns()
# processes = []
# for i in range(5):
#     process = Thread(target=do_io_job)
#     processes.append(process)
#     process.start()
# for p in processes:
#     p.join()
# end_time = time.perf_counter_ns()
# print(f"Parallel io task performed in {(end_time - start_time)/1000_000}, s")


start_time = time.perf_counter_ns()
for i in range(5):
    do_cpu_job()
end_time = time.perf_counter_ns()
print(f"Sync cpu task performed in {(end_time - start_time)/1000_000}, s")


start_time = time.perf_counter_ns()
threads = []
for i in range(5):
    thread = Thread(target=do_cpu_job())
    threads.append(thread)
    thread.start()
for t in threads:
    t.join()
end_time = time.perf_counter_ns()
print(f"Async cpu task performed in {(end_time - start_time)/1000_000}, s")

start_time = time.perf_counter_ns()
processes = []
for i in range(5):
    process = Thread(target=do_cpu_job())
    processes.append(process)
    process.start()
for p in processes:
    p.join()
end_time = time.perf_counter_ns()
print(f"Parallel cpu task performed in {(end_time - start_time)/1000_000}, s")
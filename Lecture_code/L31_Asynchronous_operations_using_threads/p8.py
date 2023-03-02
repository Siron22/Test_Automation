import time
import threading


class Employee:

    def __init__(self):
        self.salary = 0
        #self.lock = threading.Lock()
        #self.lock = threading.RLock()
        self.lock = threading.Semaphore(2)

    def increase_salary(self):
        #self.lock.acquire(timeout=2)
        #with self.lock:
        self.lock.acquire()
        print(1)
        #self.lock.acquire()
        print(2)
        local_var = self.salary
        local_var += 100
        time.sleep(1)
        self.salary = local_var
        self.lock.release()
        #self.lock.release()



# employee = Employee()
#
# thread1 = threading.Thread(target=employee.increase_salary)
# thread2 = threading.Thread(target=employee.increase_salary)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(employee.salary)


# #########################################

def hello():
    print("Hello")

timer = threading.Timer(3, hello)
timer.start()

for i in range(6):
    print(i)
    time.sleep(1)

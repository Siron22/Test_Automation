import time
import threading
import string
string.digits + string.ascii_letters + string.punctuation

def do_job():
    s = 0
    for i in range(5):
        print(f"In child: {i}")
        s += i
        time.sleep(0.8)
    return s


class CustomThread(threading.Thread):

    def __init__(self, target, id):
        super().__init__(target=target)
        self.id = id
        self.result = None

    def run(self) -> None:
        print(f"Running thread with {self.id}")
        self.result = self._target()

    def join(self, timeout=None) -> None:
        super().join(timeout)
        return self.result



thread = CustomThread(target=do_job, id=1111)
thread.start()
print(thread.result)
result = thread.join()
print(result)
#print(thread.result)
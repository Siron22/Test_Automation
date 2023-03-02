import time
import threading


def do_job(output={}):
    s = 0
    for i in range(5):
        print(f"In child: {i}")
        s += i
        time.sleep(0.8)
    output['value'] = s
    return s

output = {}
thread = threading.Thread(target=do_job, args=(output,))
thread.start()
thread.join()
print(output)
print(output['value'])
import threading

def writer(data):
    for i in range(100):
        with open('output.txt', 'a') as f:
            f.write(f"{data}\n")

thread1 = threading.Thread(target=writer, args=('=======1111',))
thread2 = threading.Thread(target=writer, args=('*******2222',))

thread1.start()
thread2.start()
thread2.join()
thread1.join()
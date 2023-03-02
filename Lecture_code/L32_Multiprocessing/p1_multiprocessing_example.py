import multiprocessing


def do_job(n, output={}):
    s = 0
    for i in range(n):
        s += i
    print(s)
    #output['result'] = s
    output.value = s
    return s

n = 5
#output = {}  # Doesn't work
#output = multiprocessing.Manager().dict()
output = multiprocessing.Value('i')
process = multiprocessing.Process(target=do_job, args=(n, output))
process.start()
process.join()
print(output)
print(output.value)

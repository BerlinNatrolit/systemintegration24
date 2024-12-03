import time
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print("sleep " + str(sec) + " second")
    time.sleep(sec)
    return "Done sleeping"
    

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
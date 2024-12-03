import time
import threading

start = time.perf_counter()

def do_something(sec):
    print("sleep " + str(sec) + " second")
    time.sleep(sec)
    print("Done sleeping")
    
threads = []
for _ in range(10):
    thread = threading.Thread(target=do_something, args=[2])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
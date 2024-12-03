import time
import threading

start = time.perf_counter()

def do_something():
    print("sleep 1 second")
    time.sleep(1)
    print("Done sleeping")
    
threads = []
for _ in range(10):
    thread = threading.Thread(target=do_something)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
import time
import threading

start = time.perf_counter()

def do_something():
    print("sleep 1 second")
    time.sleep(1)
    print("Done sleeping")
    
thread1 = threading.Thread(target=do_something)
thread2 = threading.Thread(target=do_something)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
import time

start = time.perf_counter()

def do_something():
    print("sleep 1 second")
    time.sleep(1)
    print("Done sleeping")
    
do_something()
do_something()

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
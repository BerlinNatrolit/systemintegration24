import time
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print("sleep " + str(sec) + " second")
    time.sleep(sec)
    return "Done sleeping"
    
secs = [5,4,3,2,1]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_something, secs)	# map returns result instead of futures

    for result in results:
        print(result)

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
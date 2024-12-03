import time
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print("sleep " + str(sec) + " second")
    time.sleep(sec)
    return "Done sleeping"
    

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]	# list comprehension

    for f in concurrent.futures.as_completed(results):				# As completed.
        print(f.result())

finish = time.perf_counter()
print("Finished in " + str(finish-start) + "seconds")
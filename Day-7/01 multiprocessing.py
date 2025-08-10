import multiprocessing
import time

def job(worker, name):
    print(f"Worker {worker} is working")
    print(f"Hello, {name}!")


def incrementWithLock(count, lock):
    for _ in range(1000):
        with lock:
            count.value += 1
        time.sleep(0.001)  # Simulate some work being done

def incrementWithoutLock(count):
    for _ in range(1000):
        count.value += 1
        time.sleep(0.001)  # Simulate some work being done

if __name__ == "__main__":

    # -----------------------------------
    #        Simple multiprocessing
    # -----------------------------------

    names = ["Bob", "Charlie", "David", "Eve"]

    print(multiprocessing.cpu_count())
    processes = []

    for i, name in enumerate(names):
        p = multiprocessing.Process(target=job, args=(i, name))
        p.start()           # Start the process
        processes.append(p)

    for p in processes:
        p.join()            # Wait for all processes to finish and terminate


    # -----------------------------------
    #            Without lock
    # -----------------------------------

    c = multiprocessing.Value('i', 0)   # Shared counter using Value
    processes = [multiprocessing.Process(target=incrementWithoutLock, args=(c,)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'Final counter value (without lock): {c.value}')

    # -----------------------------------
    #              With lock
    # -----------------------------------

    lock = multiprocessing.Lock()       # Create a lock
    c = multiprocessing.Value('i', 0)
    processes = [multiprocessing.Process(target=incrementWithLock, args=(c, lock)) for _ in range(5)]
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'Final counter value (with lock): {c.value}')

    
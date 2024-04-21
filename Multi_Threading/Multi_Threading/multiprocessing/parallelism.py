# Process-based Parallelism:


import multiprocessing
import time

def worker(name):
    print(f"Worker {name} started")
    time.sleep(2)  # Simulate some work
    print(f"Worker {name} finished")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


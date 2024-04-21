import multiprocessing

def worker(shared_list, value):
    shared_list.append(value)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(shared_list, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(shared_list)





# The multiprocessing module is useful for several reasons:

# Parallel Execution: It allows you to execute tasks concurrently across multiple processes, 
# taking advantage of multi-core CPUs for improved performance.
    
# Isolation: Each process runs in its own memory space, providing isolation and preventing 
# interference between concurrent tasks.

# Scalability: It scales well with the number of CPU cores, allowing you to increase parallelism as the 
# hardware resources grow.

# Fault Tolerance: Since processes run independently, errors or crashes in one process do not affect others, 
# providing fault tolerance and robustness to the system.
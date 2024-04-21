import concurrent.futures
import time

def my_function(name):
    print(f"Thread {name} started")
    # Simulate some work
    for i in range(5):
        print(f"Thread {name} working...")
        time.sleep(1)
    print(f"Thread {name} finished")

def main():
    print("Main thread started")
    
    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        future1 = executor.submit(my_function, "1")
        future2 = executor.submit(my_function, "2")
        
        # Wait for tasks to complete
        concurrent.futures.wait([future1, future2])
    
    print("Main thread finished")

if __name__ == "__main__":
    main()




# The concurrent.futures module in Python provides a high-level interface for asynchronously executing 
# callables. It is particularly useful for concurrent execution of tasks, such as executing multiple 
# functions concurrently, performing I/O-bound operations in parallel, and parallelizing CPU-bound tasks.
    

# the concurrent.futures module simplifies the process of writing concurrent and parallel code in Python, 
# making it easier to take advantage of the full potential of modern multi-core processors and 
# improve the performance and responsiveness of your applications.







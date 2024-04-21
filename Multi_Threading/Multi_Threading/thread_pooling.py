# A thread pool is a collection of worker threads that efficiently execute asynchronous callbacks on behalf of the application.
# In Python, a Thread Pool is a group of idle threads pre-instantiated and are ever ready to be given the task.

import threading
from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Executing task {name} in thread {threading.current_thread().name}")

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [executor.submit(task, i) for i in range(5)]

if __name__ == "__main__":
    main()

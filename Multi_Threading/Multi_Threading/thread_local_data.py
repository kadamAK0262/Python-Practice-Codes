import threading

thread_local_data = threading.local()

def set_thread_local_data(value):
    thread_local_data.value = value
    print(f"Thread {threading.current_thread().name}: Set thread-local data to {value}")

def get_thread_local_data():
    print(f"Thread {threading.current_thread().name}: Thread-local data is {thread_local_data.value}")

def worker():
    set_thread_local_data(threading.current_thread().name)
    get_thread_local_data()

def main():
    threads = [threading.Thread(target=worker) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()



















# Thread-local Data:

# Thread-local data allows each thread to have its own copy of a variable, ensuring that changes made to 
# the variable in one thread do not affect its value in another thread.
# We use the threading.local() function to create a threading.local() object, which acts as a 
# namespace for thread-local data.
# The set_thread_local_data function sets the thread-local data to a specified value using the
# thread_local_data object.
# The get_thread_local_data function retrieves the thread-local data from the thread_local_data object.
# The worker function sets the thread-local data to the current thread's name using the 
# set_thread_local_data function and then retrieves it using the get_thread_local_data function.
# In the main function, we create three threads, each executing the worker function. 
# Each thread will have its own copy of the thread-local data.
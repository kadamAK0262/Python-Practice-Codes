import threading

shared_variable = 0
lock = threading.Lock()

def increment_shared_variable():
    global shared_variable
    for _ in range(1000000):
        lock.acquire()
        shared_variable += 1
        lock.release()

def main():
    thread1 = threading.Thread(target=increment_shared_variable)
    thread2 = threading.Thread(target=increment_shared_variable)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Shared variable:", shared_variable)

if __name__ == "__main__":
    main()




















# We use a Lock object from the threading module to ensure that only one thread can access the 
# shared variable at a time.
    
# Thread Synchronization with Locks:

# In this example, we have a shared variable shared_variable that multiple threads will increment 
# concurrently.
# We use a Lock object from the threading module to ensure that only one thread can access 
# the shared variable at a time.
# The increment_shared_variable function is the target function for each thread. 
# It acquires the lock, increments the shared variable by 1 for 1,000,000 times, and then releases the lock.
# In the main function, we create two threads that execute the increment_shared_variable function concurrently.
# We start both threads, wait for them to complete using the join method, and then print the 
# final value of the shared variable.
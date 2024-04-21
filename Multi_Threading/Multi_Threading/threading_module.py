# The threading module is a high-level implementation of multithreading used to deploy an application
# in Python. 

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} started")
        time.sleep(2)  # Simulate some work
        print(f"{self.name} finished")

def main():
    print("Main thread started")
    
    # Create threads
    thread1 = MyThread(name="Thread 1")
    thread2 = MyThread(name="Thread 2")
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to finish
    thread1.join()
    thread2.join()
    
    print("Main thread finished")

if __name__ == "__main__":
    main()














# Thread Class Methods:
# 1. start()
# 2. run()
# 3. join() : A join() method is used to block the execution of another code until the thread terminates.


import threading
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
    
    # Create threads
    try:
        threading.Thread(target=my_function, args=("1",)).start()
        threading.Thread(target=my_function, args=("2",)).start()
    except Exception as e:
        print(f"Error: {e}")
    
    print("Main thread finished")

if __name__ == "__main__":
    main()

import threading
import queue

def producer(queue):
    for i in range(5):
        queue.put(i)
        print("Produced", i)
    queue.put(None)  # Signal the end of production

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break  # Exit the loop when None is received
        print("Consumed", item)

def main():
    q = queue.Queue()
    producer_thread = threading.Thread(target=producer, args=(q,))
    consumer_thread = threading.Thread(target=consumer, args=(q,))
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()














# Thread Communication with Queues:

# This example demonstrates how to use a Queue object from the queue module for thread-safe 
# communication between threads.
# We have a producer thread that puts integers from 0 to 4 into a queue and a consumer 
# thread that consumes items from the queue.
# The producer thread puts each item into the queue using the put method. 
# Once it finishes producing, it puts a None sentinel value into the queue to signal the end of production.
# The consumer thread continuously consumes items from the queue using the get method. 
# It exits the loop when it receives the None sentinel value.
# In the main function, we create a queue, start both producer and consumer threads, 
# and then wait for them to finish using the join method.
import multiprocessing
import time

# Parallelizing CPU-bound Tasks:
def square(x):
    return x ** 2

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        result = pool.map(square, range(10))
    print(result)









# The multiprocessing module is a powerful tool for parallel programming in Python, 
# suitable for CPU-bound tasks, parallel algorithms, and distributed computing. 
# It allows you to leverage the full potential of modern hardware and improve the performance of 
# your applications.
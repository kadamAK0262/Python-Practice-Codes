# Decorators are a common use case of higher-order functions in Python. 
# A decorator is a function that takes another function as input and returns a new function 
# with extended functionality.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Callback functions are functions that are passed as arguments to other functions 
# and are called by those functions at a later time.


def apply_operation(operation, x, y):
    result = operation(x, y)
    print(f"The result of the operation is: {result}")

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

apply_operation(add, 3, 4)
apply_operation(multiply, 3, 4)

# Function composition involves combining two or more functions to create a new function.


def add(x):
    return x + 5

def multiply(x):
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

result = compose(add, multiply)(3)
print(result)  

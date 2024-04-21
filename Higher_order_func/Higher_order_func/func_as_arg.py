# A higher-order function is a function that takes another function as an argument or returns a 
# function as a result. This concept is rooted in functional programming and is a powerful tool for
# creating flexible and reusable code.

def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result1 = apply_operation(add, 3, 4)  
result2 = apply_operation(multiply, 3, 4)  

print(result1)  
print(result2)  












# Benefits of Higher-Order Functions
# Abstraction: Higher-order functions allow you to abstract away common patterns into reusable functions.
# Flexibility: They enable you to create more flexible and customizable code by allowing functions to be parameterized with other functions.
# Composition: Higher-order functions can be composed together, allowing you to build complex behavior from simple functions.
# Currying is the technique of converting a function that takes multiple arguments into a 
# sequence of functions that each take a single argument.

def add(x):
    def inner(y):
        return x + y
    return inner

result = add(5)(3)
print(result) 

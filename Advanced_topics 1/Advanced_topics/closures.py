# A closure is a function object that has access to variables in its lexical scope, 
# even when the function is called outside that scope.

# Closures allows functions to retain access to variables from their enclosing scope, 
# even after the outer function has finished execution. This enables the creation of functions 
# with state and behavior that persists across multiple calls.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure with outer_function
closure = outer_function(5)

# Call the closure with an argument
result = closure(3)
print(result)




# Use Cases of Closures:

# Factory Functions:
# Closures are often used to create factory functions that generate other functions with 
# preconfigured behavior.
# Memoization:
# Closures can be used to implement memoization, a technique for caching the results of 
# expensive function calls to improve performance.
# Callbacks:
# Closures are useful for defining callback functions that retain access to variables from the outer scope.
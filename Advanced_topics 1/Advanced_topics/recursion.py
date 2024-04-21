# Recursion is a programming technique where a function calls itself directly or indirectly.

#  Factoeial code using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5
result = factorial(5)
print("Factorial of 5:", result) 

# **********************************************************

#  Fibonacci Sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Generate the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ") 


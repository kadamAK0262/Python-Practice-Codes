# Memoization is a technique used to speed up the execution of functions by caching the results of 
# expensive function calls and returning the cached result when the same inputs occur again.

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

print(fibonacci(10))  # Output: 55

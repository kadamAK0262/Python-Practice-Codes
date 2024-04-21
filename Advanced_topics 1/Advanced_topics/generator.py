# Generators in Python are a convenient way to create iterators. 
# They are functions that use the yield statement to produce a sequence of values lazily, 
# one at a time, rather than storing all values in memory at once like a list. 
# This makes generators memory efficient and allows for processing of large or infinite sequences.

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
# Iterate over the generator
for value in gen:
    print(value)



#  Create a fibonacci series using generator (Yield statement)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))



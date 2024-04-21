# Using the len() method:
my_string = "Hello, World!"
length = len(my_string)
print("Method 1: Length of the string is", length)


# Using a loop to count characters:
my_string = "Hello, World!"
count = 0
for char in my_string:
    count += 1
print("Method 2: Length of the string is", count)


# Using list comprehension and sum():
my_string = "Hello, World!"
length = sum(1 for char in my_string)
print("Method 3: Length of the string is", length)
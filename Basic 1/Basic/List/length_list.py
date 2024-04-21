# 1st way 
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("Length of the list:", length)

# 2nd way
my_list = [1, 2, 3, 4, 5,6]
count = 0

for _ in my_list:
    count += 1

print("Length of the list:", count)

# 3rd way
my_list = [1, 2, 3, 4, 5]
count = 0

for _ in range(len(my_list)):
    count += 1

print("Length of the list:", count)

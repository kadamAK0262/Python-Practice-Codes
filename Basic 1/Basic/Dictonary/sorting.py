list_of_dicts = [
    {'name': 'John', 'age': 30, 'salary': 50000},
    {'name': 'luffy', 'age': 25, 'salary': 60000},
    {'name': 'zoro', 'age': 35, 'salary': 45000}
]

sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])

# Print the sorted list
print("List of dictionaries sorted by age:", sorted_list)


# *****************Example 2************************************

# Sample dictionaries
dict1 = {"apple": 3, "orange": 5, "banana": 2}
dict2 = {"lion": "roar","cat": "meow", "elephant": "trumpet", "dog": "bark"}

# Convert dictionaries to list of tuples (key, value)
list1 = list(dict1.items())
list2 = list(dict2.items())

# Sort the list based on the size of keys
sorted_list1 = sorted(list1, key=lambda x: len(x[0]))
sorted_list2 = sorted(list2, key=lambda x: len(x[0]))

# Print sorted lists
print("Sorted list 1:", sorted_list1)
print("Sorted list 2:", sorted_list2)



# Using del statement
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]

print("Dictionary after removing key:", my_dict)


# Using pop() method
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'
value = my_dict.pop(key_to_remove, None)

print("Dictionary after removing key:", my_dict)


# Using popitem() method
my_dict = {'a': 1, 'b': 2, 'c': 3}

removed_item = my_dict.popitem()

print(f"Removed item: {removed_item}")
print("Dictionary after removing key:", my_dict)

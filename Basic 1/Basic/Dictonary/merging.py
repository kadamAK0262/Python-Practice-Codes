dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dict2 into dict1
dict1.update(dict2)
print("Merged dictionary using update():", dict1)



# Using ** unpacking operator:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Merge dict2 into dict1
merged_dict = {**dict1, **dict2}
print("Merged dictionary using ** unpacking operator:", merged_dict)

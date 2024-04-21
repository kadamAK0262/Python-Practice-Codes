my_dict = {'zoro': [1, 2, 3], 'whitewolf': [2, 3, 4], 'luffy': [3, 4, 5]}

def extract_unique_values(input_dict):
    unique_values = list(set(value for values in input_dict.values() for value in values))
    return unique_values


unique_values = extract_unique_values(my_dict)

print("Original dictionary:", my_dict)
print("Unique values:", unique_values)

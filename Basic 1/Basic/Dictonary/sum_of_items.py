my_dict = {'item1': 10, 'item2': 20, 'item3': 30}

def sum_of_dictionary_items(input_dict):
    total_sum = sum(input_dict.values())
    return total_sum


result_sum = sum_of_dictionary_items(my_dict)

print("Original dictionary:", my_dict)
print("Sum of all items:", result_sum)

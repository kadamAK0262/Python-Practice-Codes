my_list = [1, 2, 3, 4, 5]

print("Original List:", my_list)

def swap_elements(my_list, index1, index2):
    # Check if indices are within the valid range
    if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
        # Swap elements using a temporary variable
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp
        return True
    else:
        return False


index_to_swap1 = int(input("Enter the index of the first element to swap: "))
index_to_swap2 = int(input("Enter the index of the second element to swap: "))

if swap_elements(my_list, index_to_swap1, index_to_swap2):
    print("List after swapping:", my_list)
else:
    print("Invalid indices. Please enter valid indices within the range of the list.")

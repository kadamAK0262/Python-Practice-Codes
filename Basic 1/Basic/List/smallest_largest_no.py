my_list = [5, 2, 8, 1, 9, 3]

def find_smallest_largest(my_list):
    if not my_list:
        return None, None  # Return None for empty list

    smallest = largest = my_list[0]

    for num in my_list:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest


smallest, largest = find_smallest_largest(my_list)

if smallest is not None and largest is not None:
    print(f"The smallest number in the list is: {smallest}")
    print(f"The largest number in the list is: {largest}")
else:
    print("The list is empty.")

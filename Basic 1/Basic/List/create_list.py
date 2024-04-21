user_input = input("Enter numbers separated by spaces: ")

# Converting the input string into a list of integers
user_list = [int(num) for num in user_input.split()]

print("User input list:", user_list)

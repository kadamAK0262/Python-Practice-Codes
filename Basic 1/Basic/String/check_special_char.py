import string

user_input = input("Enter a string: ")

def contains_special_characters(input_string):
    # Define a set of special characters
    special_characters = set(string.punctuation)

    # Check if any special character is present in the input string
    return any(char in special_characters for char in input_string)



if contains_special_characters(user_input):
    print("The string contains special characters.")
else:
    print("The string does not contain any special characters.")
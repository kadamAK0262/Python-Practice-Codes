def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

while True:
    try:
        user_input = int(input("Enter a number to check if it's a palindrome (or -1 to exit): "))
        if user_input == -1:
            print("Palindrome checker closed.")
            break
        else:
            if is_palindrome(user_input):
                print(f"{user_input} is a palindrome.")
            else:
                print(f"{user_input} is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

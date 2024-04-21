def is_armstrong(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number


while True:
    try:
        user_input = int(input("Enter a number to check if it's an Armstrong number (or -1 to exit): "))
        if user_input == -1:
            print("Armstrong number checker closed.")
            break
        elif user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            if is_armstrong(user_input):
                print(f"{user_input} is an Armstrong number.")
            else:
                print(f"{user_input} is not an Armstrong number.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        user_input = int(input("Enter a non-negative integer to calculate its factorial (or -1 to exit): "))
        if user_input < -1:
            print("Please enter a non-negative integer.")
            continue
        elif user_input == -1:
            print("Factorial calculator closed.")
            break
        else:
            result = factorial(user_input)
            print(f"The factorial of {user_input} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

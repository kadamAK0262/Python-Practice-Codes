def find_min_sum_of_factors(number):
    min_sum = 0

    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            min_sum += i
            number //= i

    if number > 1:
        min_sum += number

    return min_sum

while True:
    try:
        user_input = int(input("Enter a number to find the minimum sum of its factors (or -1 to exit): "))
        if user_input == -1:
            print("Factor sum finder closed.")
            break
        elif user_input <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            min_sum_result = find_min_sum_of_factors(user_input)
            print(f"The minimum sum of factors of {user_input} is: {min_sum_result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer greater than 0.")

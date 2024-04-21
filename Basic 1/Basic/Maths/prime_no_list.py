def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

while True:
    try:
        start = int(input("Enter the start of the interval (or -1 to exit): "))
        if start == -1:
            print("Prime number printer closed.")
            break
        end = int(input("Enter the end of the interval: "))
        if start < 0 or end < 0 or start > end:
            print("Please enter valid interval values.")
        else:
            print(f"Prime numbers in the interval [{start}, {end}]:")
            for num in range(start, end + 1):
                if is_prime(num):
                    print(num)
    except ValueError:
        print("Invalid input. Please enter valid integers for the interval.")

num = int(input("Enter the number here: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")





# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(number**0.5) + 1, 2):
#             if number % i == 0:
#                 return False
#         return True

# while True:
#     try:
#         user_input = int(input("Enter a number to check if it's a prime number (or -1 to exit): "))
#         if user_input == -1:
#             print("Prime number checker closed.")
#             break
#         elif user_input < 0:
#             print("Please enter a non-negative integer.")
#         else:
#             if is_prime(user_input):
#                 print(f"{user_input} is a prime number.")
#             else:
#                 print(f"{user_input} is not a prime number.")
#     except ValueError:
#         print("Invalid input. Please enter a non-negative integer.")

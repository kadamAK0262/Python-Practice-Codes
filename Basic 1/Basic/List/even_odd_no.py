my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_even_odd_numbers(my_list):
    even_numbers = []
    odd_numbers = []

    for num in my_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)


print_even_odd_numbers(my_list)

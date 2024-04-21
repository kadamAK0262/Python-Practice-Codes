my_list = [1, 2, 3, 4, 5]

def multiply_elements(my_list):
    result = 1
    for num in my_list:
        result *= num
    return result



product_result = multiply_elements(my_list)
print(f"The product of elements in the list {my_list} is: {product_result}")

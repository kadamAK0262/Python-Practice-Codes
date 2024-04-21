
tuple_list = [(1, 'a', 3), (2, 'b', 4), (1, 'c', 5), (3, 'd', 6), (2, 'e', 7)]

def extract_digits_from_tuples(tuple_list):
    digits = ''.join(char for tpl in tuple_list for char in str(tpl) if char.isdigit())
    return digits


result_digits = extract_digits_from_tuples(tuple_list)

print("Original list of tuples:", tuple_list)
print("Extracted digits:", result_digits)

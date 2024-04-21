# 1st way 
my_list = [1, 2, 3, 4, 5]
element_to_check = 3

if element_to_check in my_list:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")


#  2nd way

my_list = [1, 2, 3, 4, 5]
element_to_check = 3

if my_list.count(element_to_check) > 0:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")


# 3rd way 
    
my_list = [1, 2, 3, 4, 5]
element_to_check = 3

for element in my_list:
    if element == element_to_check:
        print(f"{element_to_check} exists in the list.")
        break
else:
    print(f"{element_to_check} does not exist in the list.")

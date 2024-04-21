# def print_triangle(n):
#     for i in range(1, n + 1):
#         print('*' * i)

# print_triangle(5)


n = int(input("Enter the number of rows"))         
for i in range(0, n):     
        for j in range(0, i + 1):     
            print("* ", end="")         
        print()    



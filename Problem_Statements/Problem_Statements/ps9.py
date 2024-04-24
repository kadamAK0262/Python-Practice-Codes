# Problem statement 9: Given an integer n, generate the first n rows of Pascal's triangle.



n = 5
def generate(num_rows):
    triangle = []
    for row_num in range(num_rows):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))

print("Pascal's triangle with", n, "rows:")
generate(n)


# n = 5
# def generate(num_rows):
#     triangle = []
#     for row_num in range(num_rows):
#         row = [1] * (row_num + 1)
#         for j in range(1, row_num):
#             row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#         triangle.append(row)
#     return triangle

# print("Pascal's triangle with", n, "rows:")
# for row in generate(n):
#     print(row)



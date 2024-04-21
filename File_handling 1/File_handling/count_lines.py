
# with open(r"file_handling.txt", 'r') as fp:
#     lines = len(fp.readlines())
#     print('Total Number of lines:', lines)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Using for loop :
line_count = 0

with open("file_handling.txt", "r") as file:
    for line in file:
        line_count += 1
print("Number of lines in the file:", line_count)
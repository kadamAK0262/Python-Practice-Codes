# Python file handling refers to the operations performed on files, 
# such as reading from and writing to files.

# To open a file in Python, you can use the built-in open() function. 
# The open() function returns a file object, which is used to perform operations such as reading 
# from or writing to the file. It takes two arguments: the filename and the mode.

# Open a file in read mode ("r")
file = open("file_handling.txt", "r")

# Read the entire contents of the file
content = file.read()
print(content)

# Close the file
file.close()



# Python also supports the with statement for file handling. 
# It automatically closes the file when the block inside the with statement is exited.

# with open("file_handling.txt", "r") as file:
#     content = file.read()
#     print(content)


# read(): Reads the entire contents of the file.
# readline(): Reads a single line from the file.
# readlines(): Reads all lines from the file and returns them as a list.

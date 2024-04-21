# write data to files using the file object's write() method. Neer to add "w" in parameter for write.

# Open a file in write mode
file = open("file_handling.txt", "w")

# Write data to the file
file.write("Hello my name is Akshay Kadam!\n")
file.write("I'm from the great holy land of Raigad, Maharashtra..")

# Close the file
file.close()

# Write file using with statement.

# with open("file_handling.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample text file.\n")
#     file.write("Python file handling is fun!")
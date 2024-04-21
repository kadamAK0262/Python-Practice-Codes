# To append data to an existing file, you can open the file in append mode using "a" as 
# the mode argument to the open() function.

# Open a file in append mode
file = open("file_handling.txt", "a")

# Append data to the file
file.write("\nAppending additional data.")

# Close the file
file.close()

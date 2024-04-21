# Remove lines starting with a specific prefix in a text file by reading the file, 
# filtering out the lines that start with the prefix, and then writing the remaining lines back to the file.

prefix = "Hello"

# Open the input file in read mode
with open("file_handling.txt", "r") as input_file:
    # Read lines from the input file
    lines = input_file.readlines()

# Open the output file in write mode
with open("output.txt", "w") as output_file:
    # Write lines to the output file, excluding lines starting with the prefix
    for line in lines:
        if not line.startswith(prefix):
            output_file.write(line)



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      
# Read the content from one file and write it into another file.
    
# Open the input file in read mode
with open("file_handling.txt", "r") as input_file:
    # Read the content from the input file
    content = input_file.read()

# Open the output file in write mode
with open("output1.txt", "w") as output_file:
    # Write the content to the output file
    output_file.write(content)

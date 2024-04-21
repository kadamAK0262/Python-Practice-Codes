# to read file character by character
file = open('file_handling.txt', 'r')
 
while 1:
     
    # read by character
    char = file.read(1)     # we can give any number we want in one line like:- .read(5)        
    if not char: 
        break
         
    print(char)
 
file.close()




# # Open the file in read mode
# with open("file_handling.txt", "r") as file:
#     # Read the first character
#     character = file.read(1)
    
#     # Loop until the end of the file
#     while character:
#         # Process the character (e.g., print it)
#         print(character, end="")
#         # Read the next character
#         character = file.read(1)



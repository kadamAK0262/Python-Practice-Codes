# You can open files in binary mode by specifying "rb" for reading binary files and "wb" for
#  writing binary files. This is useful for working with non-text files like images or executables.


# Open a binary file for reading
with open("UseCase2.drawio.png", "rb") as file:
    data = file.read()
    print("Read binary data from the image file.")
    
    # Process binary data

# Open a binary file for writing
with open("new_image.jpg", "wb") as file:
    file.write(data)          # Write the binary data read from the original image file
    print("Binary data written to the new image file.")
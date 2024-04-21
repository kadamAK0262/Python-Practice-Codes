import json
# Open the file in read mode
with open("data.json", "r") as file:
    # Load the JSON data from the file
    data = json.load(file)
# Print the list of dictionaries
print(data)


# Change data in a JSON file.

# Modify the data
for person in data:
    if person["name"] == "Bob":
        person["age"] = 40

# Write the modified data back to the file
with open("data.json", "w") as file:
    # Write the data to the file
    json.dump(data, file, indent=4)

print(data)
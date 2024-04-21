def get_name_length(name):
    return len(name)

names = ["Akshay", "Whitewolf", "wolf", "JohnSnow"]
sorted_names = sorted(names, key=get_name_length)
print(sorted_names)  

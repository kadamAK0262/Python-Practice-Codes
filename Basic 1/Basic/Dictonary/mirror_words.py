
user_input = input("Enter a string: ")

def find_mirror_characters(input_string):
    mirror_dict = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't',
                   'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n',
                   'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h',
                   't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

    result = []

    for char in input_string:
        mirror_char = mirror_dict.get(char.lower(), char)
        result.append(mirror_char)

    return ''.join(result)


mirror_result = find_mirror_characters(user_input)

print("Original string:", user_input)
print("Mirror characters:", mirror_result)

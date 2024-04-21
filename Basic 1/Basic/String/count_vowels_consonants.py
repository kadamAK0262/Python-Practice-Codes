user_input = input("Enter a string: ")

def find_vowels_consonants(input_string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = sum(1 for char in input_string if char in consonants)

    return vowel_count, consonant_count


vowels, consonants = find_vowels_consonants(user_input)

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

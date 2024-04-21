def replace_words(input_string, words_to_replace):
    for word in words_to_replace:
        input_string = input_string.replace(word, 'A')
    return input_string

# Example usage:
original_string = "Replace apple, banana, and cherry with K."

# List of words to replace
words_to_replace = ["apple", "banana", "cherry"]

result_string = replace_words(original_string, words_to_replace)

print("Original string:", original_string)
print("Modified string:", result_string)

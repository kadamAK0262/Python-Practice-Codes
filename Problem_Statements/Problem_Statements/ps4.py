# Problem statement 4 : Given a string, determine if it is a palindrome, considering 
# only alphanumeric characters and ignoring cases.

# Input: "A man, a plan, a canal: Panama"
# Output: True
# Explanation: The string "A man, a plan, a canal: Panama" is a palindrome when ignoring cases and non-alphanumeric characters.

# Input: "race a car"
# Output: False
# Explanation: The string "race a car" is not a palindrome when ignoring cases and non-alphanumeric characters.


s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"

def isPalindrome(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

print("Is '{}' a palindrome?".format(s1), isPalindrome(s1))
print("Is '{}' a palindrome?".format(s2), isPalindrome(s2))

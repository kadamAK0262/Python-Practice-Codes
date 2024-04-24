# Problem Statement 3:
# Given a string s consisting of parentheses '(', ')', '{', '}', '[', and ']', 
# remove the minimum number of invalid parentheses in order to make the input string valid. 
# Return all possible valid strings after removing the minimum number of invalid parentheses.

s = "()())()"
def remove_invalid_parentheses(s):
    def is_valid(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def dfs(s, start, left_removed, right_removed, result):
        if left_removed == 0 and right_removed == 0:
            if is_valid(s):
                result.add(s)
            return

        for i in range(start, len(s)):
            if i != start and s[i] == s[i - 1]:
                continue

            if s[i] == '(' and left_removed > 0:
                dfs(s[:i] + s[i + 1:], i, left_removed - 1, right_removed, result)
            elif s[i] == ')' and right_removed > 0:
                dfs(s[:i] + s[i + 1:], i, left_removed, right_removed - 1, result)

    left_removed = 0
    right_removed = 0
    for char in s:
        if char == '(':
            left_removed += 1
        elif char == ')':
            if left_removed == 0:
                right_removed += 1
            else:
                left_removed -= 1

    result = set()
    dfs(s, 0, left_removed, right_removed, result)
    return list(result)

print("Valid parentheses after removal:", remove_invalid_parentheses(s))
















# Explanation:

# We define a function remove_invalid_parentheses that takes a string s as input.
# Inside the function, we define another helper function is_valid to check if a string s contains valid parentheses. This function counts the number of open and close parentheses encountered and ensures that the number of close parentheses never exceeds the number of open parentheses at any point.
# We also define a second helper function dfs (depth-first search) to recursively explore all possible valid strings after removing invalid parentheses.
# We iterate through the string s to count the number of left and right parentheses that need to be removed to make the string valid. If there are excess ')' without matching '(', we count them as right_removed.
# We use DFS to explore all possible combinations of removing parentheses. At each step, we consider removing a parenthesis if it's either a redundant ')' or a redundant '('.
# We add the valid strings obtained from DFS to a set to avoid duplicates.
# Finally, we return the list of all valid strings obtained after removal of the minimum number of invalid parentheses.
# We test the function with an example string s and print the valid parentheses after removal.
# This problem involves recursion and depth-first search and has a time complexity of O(2^N), where N is the length of the string. The space complexity is also O(2^N) due to the recursion stack and the set used to store valid strings.
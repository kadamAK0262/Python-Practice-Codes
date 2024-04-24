# Problem Statement 2 :
# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', 
# determine if the input string is valid. An input string is valid if:

# 1 Open brackets must be closed by the same type of brackets.
# 2 Open brackets must be closed in the correct order.


s = "()[]{}()"

def is_valid(s):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or stack.pop() != brackets_map[char]:
                return False
        else:
            return False

    return not stack

print("Is the string valid?", is_valid(s))

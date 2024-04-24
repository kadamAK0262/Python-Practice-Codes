# Problem Statement 1 :

# Given an array nums of n integers, find two numbers such that they add up to a specific target sum. 
# Return the indices of the two numbers as a list of two elements. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice. You can return the answer in
# any order.


# Test the function
nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

print("Indices of the two numbers:", two_sum(nums, target))
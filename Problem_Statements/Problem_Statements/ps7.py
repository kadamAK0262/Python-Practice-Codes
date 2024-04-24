# Problem statement 7: Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# Input: nums = [2, 2, 1]
# Output: 1
# Explanation: The only element that appears once is 1.

# Input: nums = [4, 1, 2, 1, 2]
# Output: 4
# Explanation: The only element that appears once is 4.


nums3 = [2, 2, 1]
nums4 = [4, 1, 2, 1, 2]

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print("The single number in {} is:".format(nums3), singleNumber(nums3))

print("The single number in {} is:".format(nums4), singleNumber(nums4))

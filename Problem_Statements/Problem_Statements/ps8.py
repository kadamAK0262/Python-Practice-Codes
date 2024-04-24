# Problem statement 8: Given an array nums, write a function to move 
# all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Input: nums = [0]
# Output: [0]

# Input: nums = [1, 0]
# Output: [1, 0]


nums1 = [0, 1, 0, 3, 12]
nums2 = [0]
nums3 = [1, 0]
num4 = [3, 0, 4, 0, 1, 5]
def moveZeroes(nums):
    zero_count = nums.count(0)
    nums[:] = [num for num in nums if num != 0]
    nums += [0] * zero_count

moveZeroes(nums1)
print("After moving zeroes, the array becomes:", nums1)

moveZeroes(nums2)
print("After moving zeroes, the array becomes:", nums2)

moveZeroes(nums3)
print("After moving zeroes, the array becomes:", nums3)

moveZeroes(num4)
print("After moving zeroes, the array becomes:", num4)


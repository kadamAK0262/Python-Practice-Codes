# Problem statement 6: Given an array nums of n integers, find all unique triplets in the 
# array which gives the sum of zero.

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: There are two unique triplets which give the sum of zero: [-1, -1, 2] and [-1, 0, 1].

# Input: nums = []
# Output: []
# Explanation: There are no triplets in an empty array.


def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

nums1 = [-1, 0, 1, 2, -1, -4]
print("Unique triplets in {} with sum zero are:".format(nums1), threeSum(nums1))

nums2 = []
print("Unique triplets in {} with sum zero are:".format(nums2), threeSum(nums2))











# We first sort the array to simplify the process.
# We iterate through the array and use two pointers technique to find all unique
#  triplets that sum up to zero.
# We handle duplicate triplets by skipping identical elements during iteration.
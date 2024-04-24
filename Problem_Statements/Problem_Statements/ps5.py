# Problem statement 5: Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were 
# inserted in order.

# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Explanation: The target value 5 is found at index 2 in the array.

# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Explanation: The target value 2 is not found in the array, but it would be inserted at index 1 to maintain sorted order.

nums3 = [1, 3, 5, 6]
target3 = 5
target4 = 2
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print("Index of target {} in {} is:".format(target3, nums3), searchInsert(nums3, target3))

print("Index to insert target {} in {} is:".format(target4, nums3), searchInsert(nums3, target4))

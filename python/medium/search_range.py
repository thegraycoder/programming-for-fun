# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


def search_range(nums: [int], target: int) -> [int]:
    n = len(nums)
    start = -1
    end = -1
    for i in range(n):
        first_element = nums[i]
        second_element = nums[n - i - 1]
        if first_element == target and start == -1:
            start = i
        if second_element == target and end == -1:
            end = n - i - 1
    return [start, end]


print(search_range([5, 7, 7, 8, 8, 10], 8))

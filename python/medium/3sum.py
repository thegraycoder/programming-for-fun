# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums):
    sums = []
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                if [nums[i], nums[left], nums[right]] not in sums:
                    sums.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                # We need bigger numbers
                left += 1
            else:
                # We need smaller numbers
                right -= 1
    return sums


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0]))

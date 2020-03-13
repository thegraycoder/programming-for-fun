# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

#
#                             ___
#             ___            |   |____     ___
#     ___    |   |||||||||||||        |||||   |___
# ___|   |||||       |||||                        |
#  0   1   2   3   4   5    6  7   8    9   10  11

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


def trap(height):
    water = 0
    for i in range(1, len(height) - 1):
        left_highest = max(height[:i])
        right_highest = max(height[i:])
        minimum_height = min(left_highest, right_highest)
        trapped_water = minimum_height - height[i] if (minimum_height - height[i] > -1) else 0
        water += trapped_water

    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([1, 0, 1]))
print(trap([2, 1, 0, 1, 3, 2, 2, 4, 0]))
print(trap([2, 1, 0, 1, 2, 1]))

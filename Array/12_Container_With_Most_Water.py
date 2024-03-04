#https://leetcode.com/problems/container-with-most-water/description/
#11. Container With Most Water

# Best approach , beats 55.53%
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Update the max_area if current area is larger
            max_area = max(max_area, area)

            # Move the pointers inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
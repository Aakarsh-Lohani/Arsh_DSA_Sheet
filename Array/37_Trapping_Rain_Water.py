# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                ans += max_right - height[right]

        return ans
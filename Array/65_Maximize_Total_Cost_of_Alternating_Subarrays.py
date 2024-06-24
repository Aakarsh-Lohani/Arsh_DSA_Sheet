# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/description/
# 3196. Maximize Total Cost of Alternating Subarrays

from typing import List
from functools import cache
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache
        def dp(i, sign):
            if i >= len(nums):
                return 0
            return sign * nums[i] + max(dp(i+1, 1), dp(i+1, -sign))
        return dp(0, 1)
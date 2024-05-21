# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/description/
# 3153. Sum of Digit Differences of All Pairs

from typing import List
from collections import Counter
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        x = len(str(nums[0]))
        tmp = [Counter() for _ in range(x)]
        n = len(nums)
        for v in nums:
            for i in range(x):
                tmp[i][v % 10] += 1
                v //= 10
        ans = n * n * x
        for i in range(x):
            for v in tmp[i].values():
                ans -= v * v
        return ans // 2
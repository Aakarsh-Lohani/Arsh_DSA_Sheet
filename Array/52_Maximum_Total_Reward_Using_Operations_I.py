# https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
# 3180. Maximum Total Reward Using Operations I

from bisect import bisect_right
from functools import cache
from typing import List
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        v = sorted(set(rewardValues))
        @cache
        def f(x):
            i = bisect_right(v, x)
            if i == len(v):
                return x
            return max(f(x + v[j]) for j in range(i, len(v)))
        return f(0)
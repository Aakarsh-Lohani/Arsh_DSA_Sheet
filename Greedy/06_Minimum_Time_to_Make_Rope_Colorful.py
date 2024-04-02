# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
# 1578. Minimum Time to Make Rope Colorful

from typing import List 
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = max_cost = total_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                res += total_cost - max_cost
                max_cost = total_cost = 0
            max_cost = max(max_cost, cost[i])
            total_cost += cost[i]
        res += total_cost - max_cost
        return res

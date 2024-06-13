# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/description/
# 3176. Find the Maximum Length of a Good Subsequence I

   
from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        d = {v: i for i, v in enumerate(set(nums))}
        if len(d) == 1:
            return len(nums)
        
        nums = [d[x] for x in nums]
        
        m = len(d)
        dp = [[0] * m for _ in range(k + 1)]
        
        ma = [0] * (k + 1)
        idx = [-1] * (k + 1)
        
        for num in nums:
            for i in range(k, -1, -1):
                dp[i][num] += 1
                if i and dp[i-1][idx[i-1]] + 1 > dp[i][num]:
                    dp[i][num] = dp[i-1][idx[i-1]] + 1
                if dp[i][num] > ma[i]:
                    ma[i] = dp[i][num]
                    idx[i] = num
        return max(max(x) for x in dp)
    

        
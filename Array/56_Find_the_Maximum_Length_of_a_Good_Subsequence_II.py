# 3177. Find the Maximum Length of a Good Subsequence II

from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = {}
        mx1 = [0]*(k+1)
        mx1u = [0]*(k+1)
        mx2 = [0]*(k+1)
        mx2u = [0]*(k+1)
        for x in nums:
            if x not in dp:
                dp[x] = [0]*(k+1)
            ndp = [c+1 for c in dp[x]]
            for r in range(k):
                ndp[r+1] = max(ndp[r+1], mx1[r]+1)
            for r in range(k+1):
                mx1[r] = max(mx1[r], ndp[r])
            dp[x] = ndp
        ans = 0
        for v in dp.values():
            ans = max(ans, max(v))
        return ans
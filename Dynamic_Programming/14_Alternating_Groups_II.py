# https://leetcode.com/problems/alternating-groups-ii/description/
# 3208. Alternating Groups II

from typing import List
class Solution:
    def numberOfAlternatingGroups(self, A: List[int], K: int) -> int:
        N = len(A)
        A = A + A
        dp = [1] * (2 * N)
        for i in range(1, 2* N):
            if A[i] !=A[i-1]:
                dp[i] = 1 + dp[i-1]
        
        ans = 0
        for i in range(N):
            if dp[i] >= K or dp[i+N] >= K:
                ans += 1
        return ans
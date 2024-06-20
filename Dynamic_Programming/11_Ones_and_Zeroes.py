# https://leetcode.com/problems/ones-and-zeroes/description/
# 474. Ones and Zeroes

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for __ in range(len(strs) + 1)]
        
        for i in range(1, len(strs) + 1):
            zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i-1][j][k], 1 + dp[i-1][j-zeros][k-ones])
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        
        return dp[len(strs)][m][n]
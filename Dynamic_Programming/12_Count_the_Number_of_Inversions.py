# https://leetcode.com/problems/count-the-number-of-inversions/description/
# 3193. Count the Number of Inversions

from typing import List
from functools import cache
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        must = [-1] * n
        for i, j in requirements:
            must[i] = j
        @cache
        def ans(pos, inv):
            if must[pos] != -1 and must[pos] != inv:
                return 0
            if pos == n - 1:
                return 1
            return (f(pos + 1, inv) - f(pos + 1, inv + pos + 2)) % 1000000007
        @cache
        def f(pos, inv):
            if inv >= 401:
                return 0
            return (ans(pos, inv) + f(pos, inv + 1)) % 1000000007
        
        return ans(0, 0)
    

# Alt sol
from typing import List
from math import comb

MOD = 10**9 + 7

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        dp = [[0] * (401) for _ in range(n+1)]
        dp[0][0] = 1 
        
        for length in range(1, n+1):
            for inv_count in range(401):
                dp[length][inv_count] = 0
                for i in range(min(length, inv_count + 1)):
                    dp[length][inv_count] += dp[length-1][inv_count-i]
                    dp[length][inv_count] %= MOD
            
  
            for endi, cnti in requirements:
                if endi == length-1:
                    for k in range(401):
                        if k != cnti:
                            dp[length][k] = 0
        
        final_inversions = next(cnti for endi, cnti in requirements if endi == n-1)
        return dp[n][final_inversions]

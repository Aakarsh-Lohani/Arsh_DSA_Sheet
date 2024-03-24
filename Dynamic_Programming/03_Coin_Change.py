# https://leetcode.com/problems/coin-change/description/
# 322. Coin Change

# BEATS 92.48% of Python 3 submissions
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1 
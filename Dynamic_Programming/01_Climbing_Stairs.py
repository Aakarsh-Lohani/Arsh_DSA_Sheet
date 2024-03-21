# https://leetcode.com/problems/climbing-stairs/description/
# 70. Climbing Stairs

# BEATS 91% of Python 3 submissions
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step_before = 2
        two_steps_before = 1
        for i in range(2, n):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        return one_step_before
    
# BEATS 23% of Python 3 submissions

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

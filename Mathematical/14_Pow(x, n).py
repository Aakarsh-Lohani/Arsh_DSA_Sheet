# https://leetcode.com/problems/powx-n/description/
# 50. Pow(x, n)

#Time Complexity : O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

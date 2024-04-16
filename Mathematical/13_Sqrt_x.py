# https://leetcode.com/problems/sqrtx/description/
# 69. Sqrt(x)

#Using Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2

        while l <= r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1

        return r
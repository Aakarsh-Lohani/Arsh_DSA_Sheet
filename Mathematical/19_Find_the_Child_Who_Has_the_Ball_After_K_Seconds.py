# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
# 3178. Find the Child Who Has the Ball After K Seconds

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k1=(k)%(n+(n-2))
        if k1> (n-1):
            return (n-1) - (k1- (n-1))
        return k1
        
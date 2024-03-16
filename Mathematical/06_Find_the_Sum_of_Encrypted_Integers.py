# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
# 3079. Find the Sum of Encrypted Integers
# Beats 100% of python3 submissions
from typing import List
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            s=str(i)
            l=len(s)
            m=int(s[0])
            for j in s:
                if int(j)>m:
                    m=int(j)
            sum+=int(l*str(m))
        return sum
        
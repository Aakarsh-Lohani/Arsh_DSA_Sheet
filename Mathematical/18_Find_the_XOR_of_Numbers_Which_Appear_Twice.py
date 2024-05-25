# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/
# 3158. Find the XOR of Numbers Which Appear Twice

from typing import List
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s=set()
        c=0
        for i in nums:
            if i in s:
                if c==0:
                    x=i
                    c=1
                else:
                
                    x=x^i
            else:
                s.add(i)
        if c==1:
            return x
        else:
            return 0
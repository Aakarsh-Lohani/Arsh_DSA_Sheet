# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/
# 3201. Find the Maximum Length of Valid Subsequence I

from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        m=0
        odd=0
        even=0
        c1="even"
        c2="odd"
        c1m=0
        c2m=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                even+=1
                if c2=="even":
                    c2m+=1
                    c2="odd"
                if c1=="even":
                    c1m+=1
                    c1="odd"

            else:
                odd+=1
                if c2=="odd":
                    c2m+=1
                    c2="even"
                if c1=="odd":
                    c1m+=1
                    c1="even"
                

        m1=even
        m2=odd
        m3=c1m
        m4=c2m

        m=max(m1,m2,m3,m4)
        return m

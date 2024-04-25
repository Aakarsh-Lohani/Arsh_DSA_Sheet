# https://leetcode.com/problems/missing-number/description/
# 268. Missing Number

#Binary search
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)
        while l<r:
            m=(l+r)//2
            if nums[m]>m:
                r=m
            else:
                l=m+1
        return l



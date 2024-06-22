# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/
# 3192. Minimum Operations to Make Binary Array Elements Equal to One II

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opr=0
        idx1=float("inf")
        for i in range(len(nums)):
            if i<idx1 :   #problem if its 0 and not in the flipped range
                if nums[i]==0:
                    idx1=i
                    opr+=1
            elif i>idx1 :   #problem if its one and in the flipped range
                if nums[i]==1:
                    idx1=float("inf")
                    opr+=1
        return opr

# Alt sol
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = cur = 0
        for i in nums:
            if (i ^ cur) == 0:
                res += 1
                cur ^= 1
        return res
                
        
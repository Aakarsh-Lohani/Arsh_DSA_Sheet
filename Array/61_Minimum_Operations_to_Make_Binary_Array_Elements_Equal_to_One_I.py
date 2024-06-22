# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opr=0
        for i in range(len(nums)):
            if nums[i]==0 and (i+2) <= (len(nums)-1):
                opr+=1
                # print("fliping",i)
                nums[i]=1
                if nums[i+1]==1:
                    nums[i+1]=0
                elif nums[i+1]==0:
                    nums[i+1]=1
                
                if nums[i+2]==1:
                    nums[i+2]=0
                elif nums[i+2]==0:
                    nums[i+2]=1
                
                # print(nums)
            elif nums[i]==0 and (i+2) > (len(nums)-1):
                return -1
        return opr
    

# Alt sol

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                res += 1
        if 0 in nums:
            return -1
        return res
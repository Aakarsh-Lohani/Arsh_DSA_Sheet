#https://leetcode.com/problems/two-sum/description/
# 1. Two Sum

#brute force
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    return list([i,j])
"""
#use hash map
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]]=i


"""
Runtime
52
ms
Beats
92.13%
of users with Python3
Memory
17.70
MB
Beats
70.26%
of users with Python3
"""
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
# 3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opr=0
        for i in range(len(nums)):
            rem=nums[i]%3
            if rem==1 or rem==2:
                opr+=1
        return opr
    

# Alt sol
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(i % 3 != 0 for i in nums)
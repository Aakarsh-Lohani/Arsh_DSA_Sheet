# https://leetcode.com/problems/maximum-prime-difference/description/
# 3115. Maximum Prime Difference

from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        d=0
        f=0
        for i in range(len(nums)):
            p=0
            if nums[i]>1:
                p=1
                n=nums[i]//2
                for j in range(2,(n)+1):
                    if nums[i]%j==0:  
                        p=0
                        break
            if p:
               
                if f==0:
                    pos=i
                    f=1
                    
                else:
                    d=i-pos
                  
        return d
                    
                
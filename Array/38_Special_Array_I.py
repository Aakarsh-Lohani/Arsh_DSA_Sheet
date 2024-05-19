# https://leetcode.com/problems/special-array-i/description/
# 3151. Special Array I

from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def odd(n):
            if n%2!=0:
                return True
        def even(n):
            if n%2==0:
                return True
            
        # [4,3,1,6]
        i=nums[0]
        if odd(i):
            for num in range(1,len(nums)):
                if num%2==0:
                    if even(nums[num]):
                        return False
                else:
                    if odd(nums[num]):
                        return False
            return True
        elif even(i):
            for num in range(1,len(nums)):
                if num%2==0:
                    if odd(nums[num]):
                        return False
                else:
                    if even(nums[num]):
                        return False
            return True
                
                
        
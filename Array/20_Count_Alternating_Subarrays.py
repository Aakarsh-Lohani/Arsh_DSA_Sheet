# https://leetcode.com/problems/count-alternating-subarrays/description/
# 3101. Count Alternating Subarrays

from typing import List
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count=0
        count+=len(nums)
        len1=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                if len1==0:
                    len1+=2
                
                else: 
                    len1+=1
          
            else:
                count+=((len1)*(len1+1)/2)-len1
                len1=0
        if len1:
            count+=((len1)*(len1+1)/2)-len1
        return int(count)
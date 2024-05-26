# https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
# 3162. Find the Number of Good Pairs I

from typing import List
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%(nums2[j]*k)==0:
                    
                    res+=1
        return res
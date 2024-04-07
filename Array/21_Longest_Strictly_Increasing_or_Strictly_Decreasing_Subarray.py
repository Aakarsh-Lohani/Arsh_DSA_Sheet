# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res=0
        inc=0
        ini=0
        dec=0
        de=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if de==1:
                    dec+=1
                elif ini==1:
                    if inc>res:
                        res=inc
                    inc=0
                    ini=0
                    dec=2
                    de=1
                elif de==0:
                    de=1
                    dec=2
            elif nums[i]<nums[i+1]:
                if ini==1:
                    inc+=1
                elif de==1:
                    if dec>res:
                        res=dec
                    dec=0
                    de=0
                    inc=2
                    ini=1
                elif ini==0:
                    ini=1
                    inc=2
            else:
                ini=de=0
                res=max(res,inc,dec)
                inc=dec=0
                
                
        if inc>res and dec==0:
            res=inc
        elif dec>res and inc==0:
            res=dec
        elif res==0 and nums:
            res=1
        return res
        
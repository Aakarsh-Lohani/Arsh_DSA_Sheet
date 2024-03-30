# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/
# 3095. Shortest Subarray With OR at Least K I

from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l=r=0
        cur_or=0
        minLen=float('inf')
        while r<len(nums):
            cur_or |=nums[r]
            while cur_or>=k and l<=r:
                minLen=min(r-l+1,minLen)
                l+=1
                cur_or=0
                for i in range(l,r+1):
                    cur_or |= nums[i]
            r+=1
        return -1 if minLen==float('inf') else minLen
# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/description/
# 3080. Mark Elements on Array by Performing Queries

import heapq
from typing import List
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        
        total = sum(nums)
        h = []
        marked = [False] * N
        
        for index, x in enumerate(nums):
            heapq.heappush(h, (x, index))
            
        ans = []
        
        for i, k in queries:
            if not marked[i]:
                total -= nums[i]
                marked[i] = True
            
            while k > 0 and len(h) > 0:
                x, index = heapq.heappop(h)
                
                if not marked[index]:
                    k -= 1
                    marked[index] = True
                    total -= x
            ans.append(total)
        return ans
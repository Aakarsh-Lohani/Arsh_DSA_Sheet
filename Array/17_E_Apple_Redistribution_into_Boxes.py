# https://leetcode.com/problems/apple-redistribution-into-boxes/description/
# 3074. Apple Redistribution into Boxes

from typing import List
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a=0
        for i in apple:
            a+=i
        capacity.sort()
        req=0
        for i in range(len(capacity)-1,-1,-1):
            req+=1
            a-=capacity[i]
            if a<=0:
                return req
        
        
        
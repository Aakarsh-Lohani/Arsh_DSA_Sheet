# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
# 3159. Find Occurrences of an Element in an Array

from typing import List
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        d={}
        occ=0
        for i in range(len(nums)):
            if nums[i]==x:
                occ+=1
                d[occ]=i
                
        # print(d)
        li=[]
        
        for q in queries:
            if q>occ:
                li.append(-1)
            else:
                li.append(d[q])

        return li
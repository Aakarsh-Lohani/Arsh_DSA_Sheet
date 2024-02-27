#https://leetcode.com/problems/find-the-duplicate-number/description/

#287. Find the Duplicate Number
#MY
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l=[0 for j in range (0,n)]
        for i in nums:
            if l[i-1]==0:
                l[i-1]=1
            else:
                return i
            
"""
Runtime
436
ms
Beats
97.45%
of users with Python3
Memory
30.79
MB
Beats
59.12%
of users with Python3
"""
            
if __name__=="__main__":
    s=Solution()
    print(s.findDuplicate([1,3,4,2,2]))
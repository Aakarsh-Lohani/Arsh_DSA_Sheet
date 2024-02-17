# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# 26. Remove Duplicates from Sorted Array
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last=nums[0]
        k=1
        dup=k
        for i in range(len(nums)):
            if nums[i]!=last: # new element
                k+=1
                last=nums[i]
                nums[dup]=last
                dup+=1
            elif (nums[i]==last):
                dup=k
        return k
"""
Runtime
72
ms
Beats
81.59%
of users with Python3

Memory
18.02
MB
Beats
62.18%
of users with Python3
"""
if __name__=="__main__":
    s=Solution()
    nums=[1,1,2]
    no=s.removeDuplicates(nums)
    print("Number of unique elements:",no)
    for i in range(no):
        print(nums[i], end=" ")
    print()
    
    nums=[0,0,1,1,1,2,2,3,3,4]
    no=s.removeDuplicates(nums)
    print("Number of unique elements:",no)
    for i in range(no):
        print(nums[i], end=" ")
   
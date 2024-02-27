#https://leetcode.com/problems/move-zeroes/description/
#283. Move Zeroes

# BEST SOLUTION
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)  # length of the list
        zeros=[]    # list to store zeros
        curr=0      # current index
        for i in range(l):      # iterate through the list
            if nums[i]==0:      # if element is zero
                zeros.append(0)
            else:
                nums[curr]=nums[i]      # copy non-zero element to the front
                curr+=1
        nums[curr:]=zeros      # append zeros to the end

""" 
Runtime
114
ms
Beats
97.75%
of users with Python3
Memory
18.16
MB
Beats
64.43%
of users with Python3
"""
# Slower but better memory usage
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)
        curr=0      # current index
        for i in range(l):      # iterate through the list
            if nums[i]!=0:
                nums[curr]=nums[i]      # copy non-zero element to the front
                curr+=1
        nums[curr:]=[0 for i in range(l-curr)]      # append zeros to the end
        """

if __name__=="__main__":
    s=Solution()
    nums=[0,1,0,3,12]
    s.moveZeroes(nums)
    print(nums)
    nums=[0]
    s.moveZeroes(nums)
    print(nums)
    
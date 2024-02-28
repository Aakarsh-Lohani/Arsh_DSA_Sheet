#https://leetcode.com/problems/sort-colors/description/
#75. Sort Colors
#inplace 
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1


"""
#need correction

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        #Do not return anything, modify nums in-place instead.
"""
        j=0
        l=len(nums)
        k=l-1
        for i in range(l):
            if nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
            elif nums[i]==2:
                if nums[k]==0:
                    if i==j:
                        nums[i],nums[k]=nums[k],nums[i]
                        k-=1
                        j+=1
                    elif i>j:
                        nums[j]=0
                        nums[i]=1
                        nums[k]=2
                        k-=1
                        j+=1
                elif nums[k]==1:
                    nums[i],nums[k]=nums[k],nums[i]
                    k-=1
                else:
                    while nums[k]==2 and k>i:
                        k-=1
                    nums[i],nums[k]=nums[k],nums[i]
                    print(nums)
                    print(i,j,k)
                    i-=3
                    print(i,j,k)
            if i>=k:
                break

"""

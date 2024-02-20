#https://leetcode.com/problems/merge-sorted-array/description/
#88. Merge Sorted Array
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[:n]
         
    



if __name__=="__main__":
    s= Solution()
    m=1
    n=0
    nums1=[1]
    nums2=[]
    s.merge(nums1,m,nums2,n)
    print(nums1)
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1,m,nums2,n)
    print(nums1)

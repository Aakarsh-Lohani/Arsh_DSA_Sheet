# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# 442. Find All Duplicates in an Array

# BEATS 73% of Python 3 submissions
# time complexity of O(n) and a space complexity of O(n)
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        count=[0]*len(nums)
        for i in range(len(nums)):
            count[nums[i]-1]+=1
            if count[nums[i]-1]==2:
                res.append(nums[i])
        return res
    
# beats 51% of Python 3 submissions
#  time complexity of O(n), but its space complexity is O(1)
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return duplicates
    
# BEATS 59% of Python 3 submissions
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=10**5+3
        ans=[]
        for x in nums:
            next=(x%p)-1
            if nums[next]>p:
                ans.append(next+1)
            nums[next]+=p
        return ans
        
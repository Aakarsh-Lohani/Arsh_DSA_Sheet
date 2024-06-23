# https://leetcode.com/contest/weekly-contest-403/problems/minimum-average-of-smallest-and-largest-elements/description/
# 3194. Minimum Average of Smallest and Largest Elements

from typing import List
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l=len(nums)
        avg=[]
        for i in range(int(len(nums)/2)):
            avg.append((nums[i]+nums[l-i-1])/2)
        return min(avg)

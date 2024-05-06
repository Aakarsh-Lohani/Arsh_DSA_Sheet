# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# 34. Find First and Last Position of Element in Sorted Array

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:  
            return [-1, -1]

        def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2 + 1  # Make m biased to the r
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        first, last = findFirst(nums, target), findLast(nums, target)
        return [first, last]
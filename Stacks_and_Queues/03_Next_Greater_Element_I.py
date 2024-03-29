# https://leetcode.com/problems/next-greater-element-i/description/
# 496. Next Greater Element I

# Beats 98% of Python 3 submissions
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = d.get(nums1[i], -1)
        return nums1
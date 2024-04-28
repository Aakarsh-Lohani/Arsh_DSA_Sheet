# https://leetcode.com/problems/find-the-integer-added-to-array-i/
# 3131. Find the Integer Added to Array I

from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0]-nums1[0]
        
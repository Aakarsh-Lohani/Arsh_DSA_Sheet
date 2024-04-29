# https://leetcode.com/problems/find-the-integer-added-to-array-ii/
# 3132. Find the Integer Added to Array II


from typing import List
import bisect
# Check time complexity ((FASTER)) 
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        ans = float('-inf')
        nums1.sort()
        nums2.sort()
        for diff in [nums1[0] - nums2[0], nums1[1] - nums2[0], nums1[2] - nums2[0]]:
            flag = True
            lo = 0
            for num2 in nums2:
                num1 = num2 + diff
                idx = bisect.bisect_left(nums1, num1, lo = lo)
                if idx >= m or nums1[idx] != num1:
                    flag = False
                    break
                lo = idx + 1
            if flag:
                ans = max(ans, diff)
        return -ans
            
        
# Check time complexity 
from typing import List
from collections import Counter
import heapq
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min2 = min(nums2)
        c, b, a = [min2 - val for val in heapq.nsmallest(3, nums1)]
        nums2 = Counter(nums2)
        for x in (a, b, c):
            if nums2 <= Counter(val + x for val in nums1):
                return x  
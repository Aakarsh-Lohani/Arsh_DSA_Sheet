# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/description/
# 3164. Find the Number of Good Pairs II
"""
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 
 """


from collections import Counter
from typing import List
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c1 = Counter(nums1)
        c2 = Counter()
        for x in nums2:
            c2[x * k] += 1
        m = max(c1)
        ans = 0
        for x in c2:
            for y in range(x, m + 1, x):
                if y in c1:
                    ans += c1[y] * c2[x]
        return ans

"""
The time complexity of this solution is O(n*m), where n is the length of nums1 and m is the maximum number in nums1. The space complexity is O(n+m), where n is the length of nums1 and m is the length of nums2.
"""
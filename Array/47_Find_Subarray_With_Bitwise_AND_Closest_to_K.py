# https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/description/
# 3171. Find Subarray With Bitwise AND Closest to K

from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        p = set([nums[0]])
        ans = abs(k - nums[0])
        for x in nums:
            p = set([x] + [x & y for y in p])
            for y in p:
                cur = abs(k - y)
                if cur < ans:
                    ans = cur
        return ans
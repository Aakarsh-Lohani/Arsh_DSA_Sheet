# https://leetcode.com/problems/special-array-ii/description/
# 3152. Special Array II

from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        acc = [0]
        n = len(nums)
        for i in range(1, n):
            acc.append(acc[-1] + (nums[i] + nums[i-1]) % 2)
        ans = []
        for l, r in queries:
            if acc[r] - acc[l] != r - l:
                ans.append(False)
            else:
                ans.append(True)
        return ans

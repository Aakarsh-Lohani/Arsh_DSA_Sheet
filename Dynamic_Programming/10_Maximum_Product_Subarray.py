# https://leetcode.com/problems/maximum-product-subarray/description/
# 152. Maximum Product Subarray

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = min_prod = res = nums[0]

        for num in nums[1:]:
            temp = max_prod
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp * num, min_prod * num)
            res = max(res, max_prod)

        return res
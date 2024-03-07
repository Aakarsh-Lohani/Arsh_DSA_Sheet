#https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#974. Subarray Sums Divisible by K

from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}  # for the subarray with sum = 0
        prefix = 0
        total = 0
        for num in nums:
            prefix = (prefix + num) % k
            if prefix < 0:  # handle negative numbers
                prefix += k
            total += count.get(prefix, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return total



"""
#2 SLOW
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        count = [0] * k
        count[0] = 1  # for the subarray with sum = 0
        for i in range(1, len(nums) + 1):
            prefix[i] = (prefix[i - 1] + nums[i - 1]) % k
            if prefix[i] < 0:  # handle negative numbers
                prefix[i] += k
            count[prefix[i]] += 1
        return sum(c * (c - 1) // 2 for c in count)
"""
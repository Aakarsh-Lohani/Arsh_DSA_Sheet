# https://leetcode.com/problems/permutations/description/
# 46. Permutations

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            # if we are at the end of the array, we have a permutation
            if start == end:
                output.append(nums[:])
            for i in range(start, end):
                # swap the current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                # generate all permutations for the next elements
                backtrack(start + 1, end)
                # backtrack, swap them back
                nums[start], nums[i] = nums[i], nums[start]

        output = []
        backtrack(0, len(nums))
        return output
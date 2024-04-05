# https://leetcode.com/problems/combination-sum-ii/description/
# 40. Combination Sum II

# Beats 98.83% of Python submissions
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:  # Skip duplicates
                    continue
                if candidates[i] > target:  # Sorted array, so no need to check further
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  # Sort the array to handle duplicates
        result = []
        backtrack(0, target, [])
        return result
    
#  bottleneck in this code is the generation of all combinations, which is unavoidable
# . The time complexity of this solution is O(2^n), where n is the number of candidates. This is because in the worst case, the algorithm needs to explore each subset of the candidates. The space complexity is O(n) to store the recursion stack.
# https://leetcode.com/problems/combinations/description/
# 77. Combinations

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
# Time complexity: O(k * C(n, k)), where C(n, k) is the number of combinations of n elements taken k at a time.
#For each combination, we spend O(k) time to process it (for example, to add it to the output list).
# Therefore, the total time complexity is O(n choose k * k).
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(1, [])
        return result

"""
# Another way to write the same code
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output
"""
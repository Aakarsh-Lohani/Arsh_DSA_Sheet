#https://leetcode.com/problems/jump-game/description/
#55. Jump Game
# Greedy Although takes more time in execution than next approach
"""
The time complexity of the canJump function is 
O(n)
, where n is the number of elements in the nums list. This is because the function iterates over the list once, performing a constant amount of work for each element.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos=0  # maximum possible index
        for i,jump in enumerate(nums):
            if i>max_pos:
                return False
            elif max_pos==len(nums)-1:
                return True
            max_pos= max(max_pos,i+jump)
        return True
"""
Runtime
376
ms
Beats
41.10%
of users with Python3
"""

"""
Another greedy approach
Runtime 
345
ms
Beats
86.32%
of users with Python3
Memory
17.83
MB
Beats
72.04%
of users with Python3
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True

# Dynamic
"""
In this solution, good_index keeps track of the leftmost "good" index. We iterate backwards through the array, and for each position, we check if there exists a jump that reaches the good_index. If there does, we update good_index to the current position. Finally, we check if the beginning of the array is a "good" index.

This solution is less efficient than the greedy approach because it requires a full pass through the array for each element, so its time complexity is 
O(n^2)
, where n is the number of elements in the array. However, it is a valid approach that correctly solves the problem.
from typing import List
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        good_index = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= good_index:
                good_index = i

        return good_index == 0
"""
343
ms
Beats
89.43%
of users with Python3
"""
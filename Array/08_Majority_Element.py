#https://leetcode.com/problems/majority-element/description/
#169. Majority Element
# Although it beats only about 20% submissions, it seems to be the best solution for this problem.
#Boyer-Moore Voting Algorithm. O(n) time and O(1) space
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)

        return candidate

#Sorting. O(nlogn) time and O(1) space
    """
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
        """
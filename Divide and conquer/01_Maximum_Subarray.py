# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum Subarray

#O(NlogN)
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Base case - when the array has only one element
        if len(nums) == 1:
            return nums[0]
        
        def findMaxCrossingSubarray(nums, left, mid, right):
            # Include at least one element from left half and one from right half
            left_sum = float('-inf')
            sum = 0
            for i in range(mid, left-1, -1):
                sum += nums[i]
                if sum > left_sum:
                    left_sum = sum
            
            right_sum = float('-inf')
            sum = 0
            for i in range(mid + 1, right + 1):
                sum += nums[i]
                if sum > right_sum:
                    right_sum = sum
            
            return left_sum + right_sum
        
        def findMaximumSubarray(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_sum = findMaximumSubarray(nums, left, mid)
            right_sum = findMaximumSubarray(nums, mid + 1, right)
            cross_sum = findMaxCrossingSubarray(nums, left, mid, right)
            
            return max(left_sum, right_sum, cross_sum)
        
        return findMaximumSubarray(nums, 0, len(nums) - 1)
    
#O(N) - Kadane's algorithm
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the second element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
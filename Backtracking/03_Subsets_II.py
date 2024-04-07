# https://leetcode.com/problems/subsets-ii/description/
# 90. Subsets II


class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # Sorting input array to handle duplicates
        
        def backtrack(start, path, result):
            result.append(path)
            
            for i in range(start, len(nums)):
                
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                backtrack(i + 1, path + [nums[i]], result)
        
        result = []
        backtrack(0, [], result)
        return result

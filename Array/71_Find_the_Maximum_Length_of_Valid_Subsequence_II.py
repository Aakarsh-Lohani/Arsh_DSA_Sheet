# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
# 3202. Find the Maximum Length of Valid Subsequence II

from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [0] * (k * k)
        def f(x, y):
            return x * k + y
        for num in nums:
            num %= k
            for i in range(k):
                if dp[f(num, i)] + 1 > dp[f(i, num)]:
                    dp[f(i, num)] = dp[f(num, i)] + 1
        return max(dp)

# class Solution:
#     def maximumLength(self, nums: List[int], k: int) -> int:
#         m=0
#         moddic=dict()
#         for i in range(1,len(nums)):
#             mod=(nums[i-1]+nums[i])%k
#             if mod not in moddic:
#                 moddic[mod]=[2,i]  #[len of valid sub,index of last valid val]
#                 print(moddic)
#             else:
#                 print("last index",moddic[mod][1])
#                 print("last val",nums[moddic[mod][1]])
#                 if (nums[moddic[mod][1]] +nums[i]) %k==mod:
#                     moddic[mod][0]+=1
#                     moddic[mod][1]=i
#                     print(moddic)
#         print("here",moddic)
#         for i in moddic.keys():
#             m=max(m,moddic[i][0])
#         print("return ",m)

#         return m

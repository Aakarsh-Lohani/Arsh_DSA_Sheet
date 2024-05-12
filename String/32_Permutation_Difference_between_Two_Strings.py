# https://leetcode.com/problems/permutation-difference-between-two-strings/description/
# 3146. Permutation Difference between Two Strings

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1={}
        m=0
        for i in range(len(s)):
            d1[s[i]]=i
        # print(d1)
        for j in range(len(t)):
            m+=abs(d1[t[j]]-j)
        return m
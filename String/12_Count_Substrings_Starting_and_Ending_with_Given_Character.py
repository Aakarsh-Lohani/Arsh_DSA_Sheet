# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/
# 3084. Count Substrings Starting and Ending with Given Character
# Beats 100% of python3 submissions
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        l=len(s)
        n=0
        total=0
        for i in range(l):
            if s[i]==c:
                n+=1
        total=int(n*(n+1)/2)
        return total
                
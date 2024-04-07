# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description/
# 3106. Lexicographically Smallest String After Operations With Constraint

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        t=""
        while k>0 and len(t)<len(s): 
            for i in range(len(s)):
                ord1=ord(s[i])-97
                d1=min(ord1,abs(ord1-26))
                if d1<=k:
                    t=t+"a"
                    k-=d1
                else:
                    t=t+chr(ord(s[i])-k)
                    k=0
        l=len(t)
        t=t+s[l:]
        return t

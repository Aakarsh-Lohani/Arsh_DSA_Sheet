# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
# 3120. Count the Number of Special Characters I

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ids=[0]*26
        idsC=[0]*26
        c=0
        for i in word:
            orv=ord(i)
            if i>="a" and i<="z":
                if idsC[orv-97]==1 and ids[orv-97]!=1:
                    c+=1
                ids[orv-97]=1
                    
            elif i>="A" and i<="Z":
                if ids[orv-65]==1 and idsC[orv-65]!=1:
                    c+=1
                idsC[orv-65]=1
        return c
                
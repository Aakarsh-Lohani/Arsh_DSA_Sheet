# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
# 3121. Count the Number of Special Characters II

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ids=[0]*26
        idsC=[0]*26
        ocr=[0]*26
        inc=[0]*26
        c=0
        for i in word:
            orv=ord(i)
            if i>="a" and i<="z":
                if idsC[orv-97]==1 and ids[orv-97]==1:
                    if ocr[orv-97]==0 and inc[orv-97]==1:
                        c-=1
                        ocr[orv-97]=1
                ids[orv-97]=1
                    
            elif i>="A" and i<="Z":
                if ids[orv-65]==1 and idsC[orv-65]!=1:
                    c+=1
                    inc[orv-65]=1
                idsC[orv-65]=1
        return c
                
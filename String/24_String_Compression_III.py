# https://leetcode.com/problems/string-compression-iii/description/
# 3163. String Compression III


class Solution:
    def compressedString(self, word: str) -> str:
        num=0
        comp=""
        last=""
        for i in word:
            if i==last:
                if num<9:
                    num+=1
                    last=i
                else:
                    comp=comp+str(num)+last
                    num=1
                    last=i
            else:
                if num>0:
                    comp=comp+str(num)+last
                    num=1
                    last=i
                else:
                    num=1
                    last=i
                    
        if num>0:
            comp=comp+str(num)+last
        return comp
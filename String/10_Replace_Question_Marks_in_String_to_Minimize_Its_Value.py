# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/description/
# 3081. Replace Question Marks in String to Minimize Its Value
# Beats 100% of python3 submissions
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        count=[0]*26
        s1=[]
        s2=""
        for i in range(len(s)):
            if s[i]!="?":
                o=ord(s[i])-97
                count[o]+=1
                
        for i in range(len(s)):
            if s[i]=="?":
                idx=count.index(min(count))
                
                s1.append(chr(idx+97))
                count[idx]+=1
            
        s1.sort()
        k=0
        for j in range(len(s)):
            if s[j]=="?":
                s2=s2+s1[k]
                k+=1
            else:
                s2=s2+s[j]
                
                
                
        return s2
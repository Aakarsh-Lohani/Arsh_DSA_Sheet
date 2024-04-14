# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/
# 3114. Latest Time You Can Obtain After Replacing Characters

class Solution:
    def findLatestTime(self, s: str) -> str:
        t=""
        if s[0]=="0":
            t=t+"0"
            if s[1]=="?":
                t=t+"9"
            else:
                t=t+s[1]
        elif s[0]=="1":
            t=t+"1"
            if s[1]=="?":
                t=t+"1"
            else:
                t=t+s[1]
        elif s[0]=="?":
            if s[1]=="0" or s[1]=="1" or s[1]=="?":
                t=t+"1"
                if s[1]=="?":
                    t=t+"1"
                else:
                    t=t+s[1]
            else:
                t=t+"0"
                t=t+s[1]
        t=t+":"
        if s[3]=="?":
            t=t+"5"
        else:
            t=t+s[3]
        if s[4]=="?":
            t=t+"9"
        else:
            t=t+s[4]
        return t
                
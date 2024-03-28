# https://leetcode.com/problems/backspace-string-compare/description/
# 844. Backspace String Compare

# Beats 96%
#  O(n) time and O(1) space
# Two pointer
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True
    

# BEATS 78%
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        t1 = ""
        for i in range(max(len(s), len(t))):
            if i >= len(s):
                if t[i] == "#" and len(t1) > 0:
                    t1 = t1[0:-1]
                elif t[i] != "#":
                    t1 = t1 + t[i]
            elif i >= len(t):
                if s[i] == "#" and len(s1) > 0:
                    s1 = s1[0:-1]
                elif s[i] != "#":
                    s1 = s1 + s[i]
            else:
                if s[i] == "#" and len(s1) > 0:
                    s1 = s1[0:-1]
                elif s[i] != "#":
                    s1 = s1 + s[i]
                if t[i] == "#" and len(t1) > 0:
                    t1 = t1[0:-1]
                elif t[i] != "#":
                    t1 = t1 + t[i]
        return s1 == t1
    

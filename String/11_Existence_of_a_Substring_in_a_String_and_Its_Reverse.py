# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/
# 3083. Existence of a Substring in a String and Its Reverse
# All 3 beats 50% of python3 submissions
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s1=s
        subs=[""]*(len(s)-1)
        for i in range(0,len(s)-1):
            sub=s[i:i+2]
            subs[i]=sub
        s1=s1[::-1]
        for j in subs:
            if j in s1:
                return True
            
        return False
"""
    SIMILAR
#2nd approach   
class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        substrings = {s[i:i+2] for i in range(len(s) - 1)}
        s1=s[::-1]
        for i in substrings:
            if i in s1:
                return True
        
        return False
        
#3rd approach
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        substrings = {s[i:i+2] for i in range(len(s) - 1)}
        return any(sub in s[::-1] for sub in substrings)
        
    """
#https://leetcode.com/problems/longest-common-prefix/description/
#14. Longest Common Prefix
# beats 78.70%
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
        return prefix
"""
# beats 60.84%
from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        
        return min(strs)
"""
"""
Correct but very slow
from typing import List 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        s=strs[0]
        for i in strs:
            if len(i)<len(s):
                s=s[0:len(i)]
            for j in range(len(i)):
                if j<len(s):
                    if s[j]!=i[j]:
                        s=s[0:j]
                        if s=="":
                            return s
                else:
                    break
        return s
"""

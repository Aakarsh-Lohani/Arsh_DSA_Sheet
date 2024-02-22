#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#28. Find the Index of the First Occurrence in a String

# Fastest beats about 96%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
"""
# beats 69%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl=len(haystack)
        l=len(needle)
        n=needle[0]
        for i in range(hl):
            if haystack[i]==n:
                if i+l<=hl:         # i+l-1 gives the index upto which needle can reach 
                                        # hl-1 gives the max index possible
                    if (haystack[i:i+l]==needle):
                        return i
        return -1
"""
"""
# Very slow but similar to the above
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        l = len(needle)
        
        for i in range(hl - l + 1):
            if haystack[i:i+l] == needle:
                return i
        
        return -1
"""

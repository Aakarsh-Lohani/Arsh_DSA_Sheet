#https://leetcode.com/problems/valid-palindrome-ii/description/
#680. Valid Palindrome 

# Correct but very slow
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali_range(i: int, j: int) -> bool:
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True


"""
#Require some correction
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=len(str)
        li=[]
        d=0
        for i in range(l//2):
            li.append(str[i])
        if l%2==0:
            for j in range(l//2,l):
                if str[j]!=li.pop():
                    d+=1
                    if d>1:
                        return False
            return True
        else:
            for j in range(l//2+1,l):
                if str[j]!=li.pop():
                    d+=1
                    if d>1:
                        return False
            return True
"""
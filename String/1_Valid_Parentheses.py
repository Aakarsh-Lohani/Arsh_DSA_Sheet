#https://leetcode.com/problems/valid-parentheses/description/
#20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i in ["{","[","("]:
                li.append(i)
            elif i in ["]","}",")"]:
                if len(li)>0:
                    j=li.pop()
                    s1=j+i
                    if s1 not in ["{}","[]","()"]:
                        return False
                else:
                    return False
        if len(li)>0:
            return False
        return True
    
if __name__=="__main__":
    s= Solution()
    print(s.isValid("()"))             # True
    print(s.isValid("()[]{}"))         # True
    print(s.isValid("(])"))            # False
    print(s.isValid("{()}"))           # True
    print(s.isValid("{{{()}]}"))       # False

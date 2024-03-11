# https://leetcode.com/problems/reverse-words-in-a-string/description/
# 151. Reverse Words in a String

#FASTEST SOLUTION beats 68%
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

#same
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
    
# DESCRIPTIVE VERY SLOW SOLUTION beats 5%
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]
            if (s[i] == " " or i == len(s) - 1) and word:
                words.append(word)
                word = ""
        return ' '.join(words[::-1])
"""

# Although it is O(n) time complexity, 
# it is not the fastest solution in terms of beating others
class Solution:
    def reverseWords(self, s: str) -> str:
        space=0
        s1=""
        s2=""
        for i in range(len(s)):
            if s[i]!=" ":
                s2=s2+s[i]
            if s[i]==" " and s2!="":
                space+=1
                if space==1:
                    print(s1)
                    s1=s2+s1
                    s2=""
                else:
                    s1=s2+" "+s1
                    s2=""
            if i==len(s)-1 and s2!="" and space>0:
                s1=s2+" "+s1
                s2=""
        if s2!="":
            if space==0:
                s1=s2+s1
            else:
                s1=s2+" "+s1
                s2=""

        return s1
"""

if __name__=="__main__":
    sol=Solution()
    s="EPY2giL"

    print(sol.reverseWords(s))
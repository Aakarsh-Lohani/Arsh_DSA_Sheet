# https://leetcode.com/problems/longest-palindrome/description/
# 409. Longest Palindrome

# BEATS 84.59%
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = defaultdict(int)
        length = 0
        for char in s:
            char_counts[char] += 1
            if char_counts[char] % 2 == 0:
                length += 2
        if length < len(s):
            length += 1
        return length
"""
# BEATS 50.70%
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)
        length = 0
        for count in char_counts.values():
            length += count // 2 * 2
            if length % 2 == 0 and count % 2 == 1:
                length += 1
        return length

# BEATS 50%
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1={}
        for i in s:
            if i not in dict1.keys():
                dict1[i]=1
            else:
                dict1[i]+=1
        l=0
        single=False
        for j in dict1.values():
            if j%2==0:
                l+=j
            elif single==False and j%2!=0:
                l+=j   # j-1 for chars upto even and 
                              #+1 for a single char which can be 
                               #accomodated to the middle of palindrome
                single=True
            elif single==True and j%2!=0:
                l+=j-1
        return l

# BEATS 17%
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1={}
        l=0
        single=False
        for i in s:
            if i not in dict1.keys():
                dict1[i]=1
            else:
                dict1[i]+=1
                if dict1[i]==2:
                    l+=2
                    dict1[i]=0
        if 1 in dict1.values():
            l+=1
        return l
"""
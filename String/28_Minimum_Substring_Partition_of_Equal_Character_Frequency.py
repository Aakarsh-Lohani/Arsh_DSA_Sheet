# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
# 3144. Minimum Substring Partition of Equal Character Frequency
# Medium
# Given a string s, you need to partition it into one or more balanced 
# substrings
# . For example, if s == "ababcc" then ("abab", "c", "c"), ("ab", "abc", "c"), and ("ababcc") are all valid partitions, but ("a", "bab", "cc"), ("aba", "bc", "c"), and ("ab", "abcc") are not. The unbalanced substrings are bolded.

# Return the minimum number of substrings that you can partition s into.

# Note: A balanced string is a string where each character in the string occurs the same number of times.

 
#1 FASTEST
# O(n^2)
# Runtime
# 1752
# ms
# Beats
# 99.52%
# Analyze Complexity
# Memory
# 16.56
# MB
# Beats
# 86.73%

from math import inf
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n =  len(s)
        min_cnt = [inf] * (n + 1)
        min_cnt[0] = 0
        a = ord('a')
        for start in range(n):
            curr = [0] * 26
            total = 0
            nonzero = 0
            max_cnt = 0
            for i, c in enumerate(s[start:], start + 1):
                c_id = ord(c) - a
                curr[c_id] += 1
                if curr[c_id] == 1:
                    nonzero += 1
                if curr[c_id] > max_cnt:
                    max_cnt = curr[c_id]
                total += 1
                if nonzero * max_cnt == total:
                    min_cnt[i] = min(min_cnt[i], min_cnt[start] + 1)
        return min_cnt[-1]

#2
# Runtime
# 2926
# ms
# Beats
# 91.43%
# Analyze Complexity
# Memory
# 16.75
# MB
# Beats
# 62.90%

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, -1, -1):
                if s[j] not in count:
                    count[s[j]] = 1
                else:
                    count[s[j]] += 1
                freq = -1
                valid = True
                for c in count:
                    if freq < 0:
                        freq = count[c]
                    if count[c] != freq:
                        valid = False
                        break
                if valid:
                    dp[i + 1] = min(dp[i + 1], 1 + dp[j])
        return dp[-1]
    
#3
# Runtime
# 2703
# ms
# Beats
# 94.76%
# Analyze Complexity
# Memory
# 16.53
# MB
# Beats
# 86.73%

class Solution(object):
    def minimumSubstringsInPartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[n] = 0
        
        
        for i in range(n):
            fre = {}
            for j in range(i,-1,-1):
                c = s[j]
                if c not in fre:  fre[c] = 0
                fre[c] += 1
                
                flag = True
                
                num = -1
                for key in fre:
                    if num >= 0 and fre[key]!=num:
                        flag = False
                        break
                    num = fre[key]
                
                if flag:
                    dp[i] = min(dp[j-1]+1, dp[i])
                    
     #   print(dp)
        
        return dp[n-1]
    

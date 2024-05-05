# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/description/
# 3137. Minimum Number of Operations to Make Word K-Periodic

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        no=0
        d={}
        for i in range(0,len(word),k):
            w1=word[i:i+k]
            no+=1
            if w1 not in d:
                d[w1]=1
            else:
                d[w1]+=1
        m=max(list(d.values()))
        return no-m
            
            
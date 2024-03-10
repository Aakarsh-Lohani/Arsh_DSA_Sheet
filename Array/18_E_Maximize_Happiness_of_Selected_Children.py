# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/
# 3075. Maximize Happiness of Selected Children
"""
Runtime
813
ms
Beats
100.00%
of users with Python3
Memory
43.58
MB
Beats
100.00%
of users with Python3
"""
from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        h=0
        happy=happiness[0:k]
        j=1
        for i in range(k):
            h+=happy[i]
            if i+1<k:
                if happy[i+1]>0:
                    if happy[i+1]-j>=0:
                        happy[i+1]=happy[i+1]-j
                    else:
                        happy[i+1]=0
            j+=1
        return h
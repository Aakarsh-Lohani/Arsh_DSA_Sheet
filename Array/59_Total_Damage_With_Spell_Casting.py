# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/
# 3186. Maximum Total Damage With Spell Casting

from typing import List
from collections import Counter
from functools import cache
from bisect import bisect_right
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        c=Counter(power)
        k=sorted(list(c.keys()))
        @cache
        def h(i):
            
            if i==len(k):return 0
            #cast
            idx = bisect_right(k,k[i]+2)
            
            cast = k[i]*c[k[i]]+h(idx)
            dont = h(i+1)
            return max(cast,dont)
        return h(0)
            
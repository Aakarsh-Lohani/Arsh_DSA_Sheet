# https://leetcode.com/problems/minimum-levels-to-gain-more-points/
# 3096. Minimum Levels to Gain More Points

from typing import List
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        p1=p2=0
        for i in possible:
            if i==0:
                p2-=1
            else:
                p2+=1
        pos=0
        g1=False
        for j in possible:
            if p1<=p2 or not g1:
                if j==0:
                    p1-=1
                    p2+=1
                    g1=True
                else:
                    p2-=1
                    p1+=1
                    g1=True
            elif p1>p2 and g1:
                break
            pos+=1
                
        if p1>p2 and g1 and pos<=len(possible)-1:
            return pos
        else:
            return -1
        
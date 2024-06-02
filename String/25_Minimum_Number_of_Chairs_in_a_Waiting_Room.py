# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
# 3168. Minimum Number of Chairs in a Waiting Room

class Solution:
    def minimumChairs(self, s: str) -> int:
        m=0
        occ=0
        for i in s:
            if i=="E":
                occ+=1
                m=max(m,occ)
            elif i=="L":
                occ-=1
        return m
        
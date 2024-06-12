# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/
# 3175. Find The First Player to win K Games in a Row

from typing import List
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        counter=0
        max1=0
        for i in range(1,len(skills)):
            if skills[max1]>skills[i]:
                counter+=1
            else:
                counter=1
                max1=i
            if counter>=k:
                return max1
        return max1


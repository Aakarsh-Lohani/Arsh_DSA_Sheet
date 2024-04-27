# https://leetcode.com/problems/make-a-square-with-the-same-color/description/
# 3127. Make a Square with the Same Color

from typing import List
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        box=[[[0,0],[0,1],[1,0],[1,1]],
          [[2,0],[2,1],[1,0],[1,1]],
           [[0,2],[0,1],[1,2],[1,1]],
           [[2,2],[2,1],[1,2],[1,1]],
          ]
        for i in box:
            w=b=0
            for j in i:
                m,n=j
                if grid[m][n]=="W":
                    w+=1
                else:
                    b+=1
            if w>=3 or b>=3:
                return True
        return False
        
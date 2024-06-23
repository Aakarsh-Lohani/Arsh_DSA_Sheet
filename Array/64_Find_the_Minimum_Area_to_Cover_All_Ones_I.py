# https://leetcode.com/contest/weekly-contest-403/problems/find-the-minimum-area-to-cover-all-ones-i/description/
# 3195. Find the Minimum Area to Cover All Ones I

from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        area=0
        minlen=0
        maxlen=0
        minwid=0
        maxwid=0
        c=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and c==0:
                    minlen=row
                    minwid=col
                    maxlen=row
                    maxwid=col
                    c=1
                elif grid[row][col]==1 and c==1:
                    maxlen=max(row,maxlen)
                    maxwid=max(col,maxwid)
                    minlen=min(minlen,row)
                    minwid=min(minwid,col)
        # print(minlen,maxlen,minwid,maxwid)
        l=(maxlen-minlen)+1
        w=(maxwid-minwid)+1
        # print("l",l,"w",w)
        area=(l*w)
        return area
                    
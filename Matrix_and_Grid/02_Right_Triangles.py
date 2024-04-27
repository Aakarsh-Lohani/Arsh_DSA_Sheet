# https://leetcode.com/problems/right-triangles/description/
# 3128. Right Triangles

from typing import List
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n=0
        r=[0 for i in range(len(grid))]
        c=[0 for j in range(len(grid[0]))]
        t=list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    r[i]+=1
                    c[j]+=1
                    t1=[i,j]
                    t.append(t1)
        for e in t:
            i,j=e
            if grid[i][j]==1:
                if r[i]>=2 and c[j]>=2:
                    n+=(r[i]-1)*(c[j]-1)
            
        return n
            
        
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/description/
# 3111. Minimum Rectangles to Cover Points

from typing import List
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        currx=0
        curry=0
        points.sort()
        print(points)
        n=0
        i=0
        while i<= len(points)-1:
            n+=1
            currx=points[i][0]
            curry=points[i][1]
            while points[i][0]-currx<=w and i<=len(points)-1:
                i+=1
                if i==len(points):
                    break
        return n
        
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
# 3197. Find the Minimum Area to Cover All Ones II


from typing import List
from functools import cache
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        inf=float('inf')
        @cache
        def solve1(i1, i2, j1, j2):
            imin = jmin = inf
            imax = jmax = -1
            for i in range(i1, i2):
                for j in range(j1, j2):
                    if grid[i][j]:
                        imin = min(imin, i)
                        imax = max(imax, i)
                        jmin = min(jmin, j)
                        jmax = max(jmax, j)
            if imax == -1:
                return 0
            return (imax - imin + 1) * (jmax - jmin + 1)
        def solve2(i1, i2, j1, j2):
            ans = inf
            for i in range(i1+1, i2):
                ans = min(ans, solve1(i1, i, j1, j2) + solve1(i, i2, j1, j2))
            for j in range(j1+1, j2):
                ans = min(ans, solve1(i1, i2, j1, j) + solve1(i1, i2, j, j2))
            return ans
        def solve3(i1, i2, j1, j2):
            ans = inf
            for i in range(i1+1, i2):
                ans = min(ans, solve2(i1, i, j1, j2) + solve1(i, i2, j1, j2))
                ans = min(ans, solve1(i1, i, j1, j2) + solve2(i, i2, j1, j2))
            for j in range(j1+1, j2):
                ans = min(ans, solve2(i1, i2, j1, j) + solve1(i1, i2, j, j2))
                ans = min(ans, solve1(i1, i2, j1, j) + solve2(i1, i2, j, j2))
            return ans
        return solve3(0, len(grid), 0, len(grid[0]))
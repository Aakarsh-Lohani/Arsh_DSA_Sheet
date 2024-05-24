# https://leetcode.com/problems/unique-paths/description/
# 62. Unique Paths

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)
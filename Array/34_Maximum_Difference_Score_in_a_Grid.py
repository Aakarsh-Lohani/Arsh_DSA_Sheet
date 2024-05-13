"""
3148. Maximum Difference Score in a Grid

You are given an m x n matrix grid consisting of positive integers. You can move from a cell in the matrix to any other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value c1 to a cell with the value c2 is c2 - c1.

You can start at any cell, and you have to make at least one move.

Return the maximum total score you can achieve.

 """

from typing import List
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('-inf') for i in range(n)] for j in range(m)]
        ans = float('-inf')
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(dp[i][j+1] if j+1<n else float('-inf'), dp[i+1][j] if i+1<m else float('-inf'))
                ans = max(ans, dp[i][j]-grid[i][j])
                dp[i][j]=max(dp[i][j],grid[i][j])
        return ans
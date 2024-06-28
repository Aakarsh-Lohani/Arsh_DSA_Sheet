# https://leetcode.com/problems/sudoku-solver/description/
# 37. Sudoku Solver

# time complexity is (O(9^{n})), where (n) is the number of empty cells.
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board, row, col, num):
            # Check if the number is not in the current row/column/3x3 subgrid
            for x in range(9):
                if board[row][x] == num: return False
                if board[x][col] == num: return False
                if board[3*(row//3) + x//3][3*(col//3) + x%3] == num: return False
            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if isValid(board, i, j, num):
                                board[i][j] = num
                                if solve(board): return True
                                board[i][j] = '.' # Undo move
                        return False
            return True
        
        solve(board)
        """
        Do not return anything, modify board in-place instead.
        """
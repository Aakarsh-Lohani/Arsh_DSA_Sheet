# https://leetcode.com/problems/valid-sudoku/description/
# 36. Valid Sudoku

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def CheckBox(box,seen):
            if box ==".":
                return True
            if box not in seen:
                seen.append(box)
                return True
            else:
                return False

        # Check rows 
        for line in board:
            seen = [] 
            for box in line:
                if not CheckBox(box, seen):
                    return False
                
        # Check collums
        for x in range(len(board)):
            seen = []
            for y in range(len(board)):
                box = board[y][x]
                if not CheckBox(box, seen):
                    return False

        #Check 3x3s
        #get the other 8 from 3x3 from the top left
        dirs = [[1,0],[2,0],[1,1],[2,1],[0,1],[0,2],[1,2],[2,2]]
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = []
                seen.append(board[i][j]) # add the staring pos top left
                for d in dirs:
                    box = board[i+d[0]][j+d[1]]
                    if not CheckBox(box, seen):
                        return False
        return True
                

# O(1) - ALT
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))

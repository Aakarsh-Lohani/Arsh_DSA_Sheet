# https://leetcode.com/problems/generate-parentheses/description/
# 22. Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s = '', l = 0, r = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if l < n:
                backtrack(s+'(', l+1, r)
            if r < l:
                backtrack(s+')', l, r+1)

        res = []
        backtrack()
        return res
    
# The time complexity is O(4^n / sqrt(n)) due to the Catalan number, which is the number of valid parentheses expressions. The space complexity is O(n) to store the result.
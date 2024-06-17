# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/description/
# 3185. Count Pairs That Form a Complete Day II

from typing import List
from collections import defaultdict
class Solution:
    def countCompleteDayPairs(self, a: List[int]) -> int:
        ans = 0
        d = defaultdict(lambda: 0)
        for val in a:
            rem = val % 24
            need = 24 - rem
            need %= 24
            ans += d[need]
            d[rem] += 1
        return ans
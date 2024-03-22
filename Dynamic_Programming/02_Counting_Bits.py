# https://leetcode.com/problems/counting-bits/description/
# 338. Counting Bits

# Beats 69% of Python 3 submissions
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
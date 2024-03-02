#https://leetcode.com/problems/add-binary/description/
#67. Add Binary
"""
# BEST
# Using in built library function , Beats 93%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
"""

"""
# Beats 68% , slow and descriptive

"""

"""
# Beats 95% , but may run slow as may beats 17%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])
"""
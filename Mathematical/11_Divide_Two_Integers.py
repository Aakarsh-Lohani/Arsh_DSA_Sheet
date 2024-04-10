# https://leetcode.com/problems/divide-two-integers/description/
# 29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handling overflow
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = -1 if ((dividend < 0) != (divisor < 0)) else 1

        # Converting both numbers to positive
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        return sign * result
# https://leetcode.com/problems/harshad-number/
# 3099. Harshad Number

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        sum1=0
        for i in s:
            sum1+=int(i)
        if x%sum1==0:
            return sum1
        else:
            return -1
            
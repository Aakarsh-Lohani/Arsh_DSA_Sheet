# https://leetcode.com/problems/integer-to-roman/description/
#12. Integer to Roman
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#LITTLE BETTER IN MEMORY BEATS 88%
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman += numerals[i]
        return roman
"""
This solution is efficient because it only requires a single pass through the list of values and a number of iterations proportional to the size of the number for each value. Therefore, its time complexity is O(1), and its space complexity is also O(1) because it only needs a constant amount of space to store the list of values and numerals and the string.
"""
# Beats 94% MY
class Solution:
    def intToRoman(self, num: int) -> str:
        r=""
        n=num
        while n>=1000:
            r+="M"
            n-=1000
        while n>=500:
            if n>=900:
                r+="CM"
                n-=900
            else:
                r+="D"
                n-=500
        while n>=100:
            if n>=400:
                r+="CD"
                n-=400
            else:
                r+="C"
                n-=100
        while n>=50:
            if n>=90:
                r+="XC"
                n-=90
            else:
                r+="L"
                n-=50
        while n>=10:
            if n>=40:
                r+="XL"
                n-=40
            else:
                r+="X"
                n-=10
        while n>=5:
            if n==9:
                r+="IX"
                n-=9
            else:
                r+="V"
                n-=5
        while n>=1:
            if n==4:
                r+="IV"
                n-=4
            else:
                r+="I"
                n-=1
        return r

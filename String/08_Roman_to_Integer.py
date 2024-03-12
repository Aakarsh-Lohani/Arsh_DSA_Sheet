# https://leetcode.com/problems/roman-to-integer/description/
# 13. Roman to Integer
#MY BEST APPROACH BEATS 89.62%
class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        temp=0
        priority={"M":(1000,7),"D":(500,6),"C":(100,5),"L":(50,4),"X":(10,3),"V":(5,2),"I":(1,1)}
        p=0
        for i in s:
            if p==0:
                p=priority[i][1]
            if priority[i][1]==p:
                temp+=priority[i][0]
                p=priority[i][1]
            elif priority[i][1]<p:
                val+=temp
                temp=priority[i][0]
                p=priority[i][1]
            else:
                val+=priority[i][0]-temp
                temp=0
                p=priority[i][1]
        if temp:
            val+=temp
        return val
    

"""
#Slower approach by reversing the string and then iterating through it
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for c in reversed(s):
            curr_value = roman_to_int[c]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total
"""

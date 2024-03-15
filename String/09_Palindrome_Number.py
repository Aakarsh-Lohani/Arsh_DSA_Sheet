# https://leetcode.com/problems/palindrome-number/description/
# 9. Palindrome Number

# beats 98% of python3 submissions
# by reversing the number and comparing it with the original number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        s1=s
        s=s[::-1]
        if s==s1:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

s=Solution()
s.isPalindrome(121)
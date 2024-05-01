# https://leetcode.com/problems/happy-number/description/
# 202. Happy Number

#FAST
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            return sum(int(x) ** 2 for x in str(n))
        
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
    
#Slow
class Solution:
    def isHappy(self, n: int) -> bool:
        s= set()
        while n != 1 and n not in s:
            s.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

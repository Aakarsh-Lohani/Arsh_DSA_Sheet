# https://leetcode.com/problems/water-bottles-ii/
# 3100. Water Bottles II

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty=drunk=0
        drunk=numBottles
        numBottles=0
        empty=drunk
        while empty>=numExchange:
            empty-=numExchange
            drunk+=1
            empty+=1
            numExchange+=1
        return drunk
            
        
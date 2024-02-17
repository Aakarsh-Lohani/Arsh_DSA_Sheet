#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#122. Best Time to Buy and Sell Stock II
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        share=False
        buy=0
        profit=0
        l=len(prices)
        for i in range(l-1):
            if prices[i+1]>prices[i]:
                if share==False:
                    buy=i
                    share=True
            elif prices[i+1]<prices[i]:
                if share==True:
                    profit+=prices[i]-prices[buy]
                    share=False
        if share==True:
            share=False
            profit+=prices[l-1]-prices[buy]
        return profit
"""
54
ms
Beats
82.86%
of users with Python3
Memory
17.55
MB
Beats
88.11%
of users with Python3
"""
if __name__=="__main__":
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
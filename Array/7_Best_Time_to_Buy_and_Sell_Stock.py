#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#121. Best Time to Buy and Sell Stock
""" 
#Same approach #my 

from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for price in prices:
            if price<min:
                min=price
            elif price>min and price-min>profit:
                profit=price-min
        return profit
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
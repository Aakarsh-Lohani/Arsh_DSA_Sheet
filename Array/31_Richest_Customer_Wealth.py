# https://leetcode.com/problems/richest-customer-wealth/description/
# 1672. Richest Customer Wealth

from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            m1=0
            for j in i:
                m1+=j
            if m1>=m:
                m=m1
        return m

# Using sum function
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            m1=sum(i)
            if m1>=m:
                m=m1
        return m
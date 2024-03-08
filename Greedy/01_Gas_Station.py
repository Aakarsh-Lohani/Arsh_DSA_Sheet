# https://leetcode.com/problems/gas-station/description/
# 134. Gas Station
# Brute Force TLE
"""
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for station in range(len(gas)):
            tank=gas[station]
            curr=station
            while tank>=cost[curr] :
                tank-=cost[curr]
                curr=(curr+1)%len(gas)
                if curr==station:
                    return station
                tank+=gas[curr]
        return -1
"""
# Single pass
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = curr_gas = curr_cost = start_station = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas += gas[i]
            curr_cost += cost[i]
            if curr_gas < curr_cost:
                start_station = i + 1
                curr_gas = curr_cost = 0
        return start_station if total_gas >= total_cost else -1

if __name__=="__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    s=Solution()
    print(s.canCompleteCircuit(gas,cost))  #3

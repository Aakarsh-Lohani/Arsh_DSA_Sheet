# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/
# 3147. Taking Maximum Energy From the Mystic Dungeon

from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m=float('-inf')
        l=[]
         # energy = [-2,-3,-1], k = 2
        for s in range(k):
            s1=0
            for i in range(s,len(energy),k):
                if s1+energy[i]>=0:
                    s1+=energy[i]
                
                elif s1+energy[i]<=0 and i+k>=len(energy):
                    # print(s1+energy[i],i+k)
                    s1=max(s1+energy[i],energy[i])
                    # print("elif", s1)
                else:
                    
                    s1=0
                    # print("s",energy[s], "i",i)
                    # print("else")
    
            m=max(m,s1)
            # print(m ,"changed")
        
        return m
        
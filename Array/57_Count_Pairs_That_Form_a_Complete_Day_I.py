# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
# 3184. Count Pairs That Form a Complete Day I

from typing import List
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        days=0
        c=0
        # def fact2(k):
        #     c1=1
        #     for i in range(1,k+1):
        #         c1*=i
        #     c1/=2
        #     print("Adding from fact2",int(c1))
        #     return int(c1)
                
                      
        for i in range(len(hours)):
            if hours[i]%24==0 and hours[i]>=24:
                c+=1
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    days+=1
                    # print("Adding",i,j)
        
        # days+=fact2(c)
        return days
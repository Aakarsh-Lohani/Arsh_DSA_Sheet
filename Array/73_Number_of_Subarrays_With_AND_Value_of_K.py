# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/description/
# 3209. Number of Subarrays With AND Value of K

class Solution:
    def countSubarrays(self, A: List[int], target: int) -> int:
        count = {}
        ans = 0
        for x in A:
            count2 = {}
            for y, v in count.items():
                y2 = y&x
                count2[y2] = count2.get(y2,0) + v
            
            count2[x] = count2.get(x,0) + 1
            
            count = count2
            ans += count.get(target, 0)
        return ans
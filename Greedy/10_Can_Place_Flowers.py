# https://leetcode.com/problems/can-place-flowers/description/
# 605. Can Place Flowers

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        rem = n
        i = 0
        while rem > 0 and i < len(flowerbed):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                rem -= 1
                flowerbed[i] = 1
            i += 1
        return rem == 0
    
# optimized solution
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, count = 0, 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 2  # skip the next plot
            else:
                i += 1  # move to the next plot
        return count >= n
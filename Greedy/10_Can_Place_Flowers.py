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
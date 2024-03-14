# https://leetcode.com/problems/max-points-on-a-line/description/
# 149. Max Points on a Line

# 1. Beats 95.80% of python3 submissions
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        max_points = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            slopes = {}
            same_points = 0
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    same_points += 1
                else:
                    if x1 == x2:
                        slope = float('inf')
                    else:
                        slope = (y2 - y1) / (x2 - x1)
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
            if len(slopes) == 0:
                max_points = max(max_points, same_points + 1)
            else:
                max_points = max(max_points, max(slopes.values()) + same_points + 1)
        return max_points
        

# 2. Beats 64% of python3 submissions
from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points = [tuple(point) for point in points]
        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                    gcd = self.gcd(dx, dy)
                    slopes[(dx // gcd, dy // gcd)] += 1
            max_points = max(max_points, duplicates + max(slopes.values(), default=0))

        return max_points

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
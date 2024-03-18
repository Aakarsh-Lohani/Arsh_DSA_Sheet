# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
# 1743. Restore the Array From Adjacent Pairs


from collections import defaultdict
from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pair_map = defaultdict(list)
        for pair in adjacentPairs:
            pair_map[pair[0]].append(pair[1])
            pair_map[pair[1]].append(pair[0])

        for key, value in pair_map.items():
            if len(value) == 1:
                start = key
                break

        result = [start]
        while len(result) < len(adjacentPairs) + 1:
            next_val = pair_map[result[-1]].pop()
            pair_map[next_val].remove(result[-1])
            result.append(next_val)

        return result
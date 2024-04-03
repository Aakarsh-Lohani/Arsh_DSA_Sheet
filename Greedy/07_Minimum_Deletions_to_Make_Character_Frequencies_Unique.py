# https://leetcode.com/problems/minimum-deletions-to-make-character-freq-unique/description/
# 1647. Minimum Deletions to Make Character Freq Unique

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        freq = list(counter.values())
        freq.sort(reverse=True)
        
        deletions = 0
        for i in range(1, len(freq)):
            while freq[i] > 0 and freq[i] >= freq[i - 1]:
                freq[i] -= 1
                deletions += 1
                
        return deletions
    
"""
The overall time complexity of the function is O(n log n) for sorting the frequencies + O(n) for iterating over the sorted frequencies, which simplifies to O(n log n)

1. Sorting the frequencies: The sort function in Python uses a sorting algorithm called Timsort, which has a worst-case and average time complexity of O(n log n), where n is the number of frequencies.

2. Iterating over the sorted frequencies: The outer for loop runs in O(n) time, where n is the number of frequencies. The inner while loop can also run up to n times in the worst case, when all frequencies are the same. However, each time the while loop runs, it decreases the frequency by 1, which ensures that the same frequency will not be processed again. Therefore, the total time complexity of the for loop and the while loop combined is O(n), not O(n^2).

"""
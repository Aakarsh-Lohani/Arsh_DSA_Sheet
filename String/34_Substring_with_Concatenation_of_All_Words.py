# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
# Substring with Concatenation of All Words

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_counter = Counter(words)
        res = []
        
        for i in range(len(s) - total_len + 1):
            seen = Counter()
            for j in range(i, i + total_len, word_len):
                curr_word = s[j:j + word_len]
                if curr_word in word_counter:
                    seen[curr_word] += 1
                    if seen[curr_word] > word_counter[curr_word]:
                        break
                else:
                    break
            else:
                res.append(i)
        
        return res
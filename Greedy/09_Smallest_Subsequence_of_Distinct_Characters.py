# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 1081. Smallest Subsequence of Distinct Characters

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        st = []
        
        for i, c in enumerate(s):
            if c not in st:
                while st and c < st[-1] and i < last_occ[st[-1]]:
                    st.pop()
                st.append(c)
                
        return ''.join(st)
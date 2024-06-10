# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/
# 3179. Find the N-th Value After K Seconds

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        a = [1] * n
        for _ in range(k):
            cur_sum = 0
            for j in range(n):
                cur_sum = (cur_sum + a[j]) % MOD
                a[j] = cur_sum
        return a[-1]
        

# https://leetcode.com/problems/count-and-say/description/
# 38. Count and Say

# Space O(1)
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s
    
# Space O(n)
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            pre = self.countAndSay(n - 1)
            res = ''
            i = 0
            while i < len(pre):
                count = 1
                while i + 1 < len(pre) and pre[i] == pre[i + 1]:
                    i += 1
                    count += 1
                res += str(count) + pre[i]
                i += 1
            return res
        

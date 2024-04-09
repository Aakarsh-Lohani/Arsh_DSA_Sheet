# https://leetcode.com/problems/multiply-strings/description/
# 43. Multiply Strings


# Simulate the long multiplication process
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                prod = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = prod + res[p2]
                
                res[p2] = total % 10
                res[p1] += total // 10
                
        while len(res) > 0 and res[0] == 0:
            res.pop(0)
            
        return ''.join(map(str, res))
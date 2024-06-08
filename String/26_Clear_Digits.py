# https://leetcode.com/problems/clear-digits/description/
# 3174. Clear Digits

class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        res=""
        res1=[]
        # "q2qq"
        for i in range(len(s)):
            if ord(s[i])>=48 and ord(s[i])<=57:
                res1.append(i)
                if st:
                    res1.append(st[-1])
                    st.pop()
            else:
                st.append(i)
        
        # print(res1)
        
        for i in range(len(s)):
            if i not in res1:
                res=res+s[i]
            # res=res[0:i]+res[i+1+1:]
            # print(res)
        # print(res)
        return res
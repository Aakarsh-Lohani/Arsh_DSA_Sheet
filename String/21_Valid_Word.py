# https://leetcode.com/problems/valid-word/description/
# 3136. Valid Word

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)>=3:
            v=0
            c=0
            d=0
            for i in word:
                
                if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                    if i in ["a","e","i","o","u","A","E","I","O","U"]:
                        v+=1
                        # print(i,"v")
                    elif i in ["1","2","3","4","5","6","7","8","9"]:
                        # print(i,"d")
                        d+=1
                    else:
                        c+=1
                        # print(i,"c")
                else:
                    return False
                
            if v and c :
                return True
            else:
                return False
        else:
            return False
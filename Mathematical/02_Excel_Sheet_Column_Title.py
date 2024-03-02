#https://leetcode.com/problems/excel-sheet-column-title/description/
# 168. Excel Sheet Column Title
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col=""
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            col=chr(rem+65)+col
            columnNumber//=26
        return col



# REVERSE SOLUTION GIVES COLUMN NUMBER FROM COLUMN TITLE
# columnNumber="AB"  # Column Title
# col=0              # Column number
# j=0
# for i in range(len(columnNumber)-1,-1,-1):
#     o=ord(columnNumber[i])-64
#     col+=o*26**j
#     j+=1
# print(col)


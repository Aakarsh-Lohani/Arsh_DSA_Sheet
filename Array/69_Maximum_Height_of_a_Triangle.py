# https://leetcode.com/problems/maximum-height-of-a-triangle/description/
# 3200. Maximum Height of a Triangle

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        m=0
        r=red
        b=blue
        s="r"
        row=0
        for i in range(1,red+blue+1):
            if (red>0 or blue>0) :
                if s=="r" and i<=red:
                    red-=i
                    s="b"
                    row+=1
                    # print("red",i)
                elif s=="b" and i<=blue:
                    blue-=i
                    s="r"
                    row+=1
                    # print("blue",i)
                else:
                    break
            else:
                break
        m=row
        row=0
        s="b"
        red=r
        blue=b
        for i in range(1,red+blue+1):
            if (red>0 or blue>0) :
                if s=="r" and i<=red:
                    red-=i
                    s="b"
                    row+=1
                    # print("red",i)
                elif s=="b" and i<=blue:
                    blue-=i
                    s="r"
                    row+=1
                    # print("blue",i)
                else:
                    break
            else:
                break
        m=max(m,row)
        return m
            


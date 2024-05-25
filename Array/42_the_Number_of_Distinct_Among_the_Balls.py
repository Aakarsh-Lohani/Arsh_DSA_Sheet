# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
# 3160. Find the Number of Distinct Colors Among the Balls

from typing import List
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # [[1,2],[2,4],[2,2],[3,3],[1,4],[2,3],[3,1],[3,3]]
        d={}
        colors={}
        res=[]
        for ball,color in queries:
            # print("for", ball,color)
            if ball in d.keys():
                # print("ball in d")
                colors[d[ball]]-=1
                # print("old color reduced",colors[d[ball]])
                # print("colors" ,colors)
                if colors[d[ball]]==0:
                    # print("deleting color", d[ball] , "len of colors",len(colors))
                    del colors[d[ball]]
                    # print("deleted ","len of colors", len(colors))
                    
                d[ball]=color
                # print("new color updated in d")
                if color not in colors.keys():
                    colors[color]=1
                    # print("new color")
                else:
                    # print("add 1 to", colors[color] ,"for color", color)
                    colors[color]+=1
                    # print("added 1 to", colors[color])
                # print("color updated",colors)
                
            else:
                d[ball]=color
                # print("new ball")
                if color not in colors.keys():
                    colors[color]=1
                else:
                    colors[color]+=+1
                # print("colors",colors)

            res.append(len(colors))
            # print()
            # [1,2,1,2,3,2,3,2]
            # [1,2,1,2,3,2,3,2]
        return res
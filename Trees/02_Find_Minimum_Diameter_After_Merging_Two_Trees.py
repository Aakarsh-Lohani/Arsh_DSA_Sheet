# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
# 3203. Find Minimum Diameter After Merging Two Trees

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        path1 = [[] for _ in range(n1)]
        for u, v in edges1:
            path1[u].append(v)
            path1[v].append(u)
        path2 = [[] for _ in range(n2)]
        for u, v in edges2:
            path2[u].append(v)
            path2[v].append(u)
        
        def dfs1(u, p):
            for v in path1[u]:
                if v != p:
                    d[v] = d[u] + 1
                    dfs1(v, u)
        
        d1 = [0] * n1
        d = [0] * n1
        dfs1(0, -1)
        
        u = d.index(max(d))
        d[u] = 0
        dfs1(u, -1)
        
        for i in range(n1):
            d1[i] = d[i]
        
        u = d.index(max(d))
        d[u] = 0
        dfs1(u, -1)
        for i in range(n1):
            if d[i] > d1[i]:
                d1[i] = d[i]
        
        def dfs2(u, p):
            for v in path2[u]:
                if v != p:
                    d[v] = d[u] + 1
                    dfs2(v, u)
        
        d2 = [0] * n2
        d = [0] * n2
        dfs2(0, -1)
        
        u = d.index(max(d))
        d[u] = 0
        dfs2(u, -1)
        
        for i in range(n2):
            d2[i] = d[i]
        
        u = d.index(max(d))
        d[u] = 0
        dfs2(u, -1)
        for i in range(n2):
            if d[i] > d2[i]:
                d2[i] = d[i]
        return max(max(d1), max(d2), min(d1) + min(d2) + 1)
        
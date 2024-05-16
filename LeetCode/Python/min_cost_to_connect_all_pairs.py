from collections import defaultdict
from heapq import heappop, heappush



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(int)
        pq = []
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                heappush(pq,[abs(x1-x2) + abs(y1-y2),i,j])
                
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(u):
            if u==parent[u]:
                return u
            return find(parent[u])
        
        def union(u,v):
            x,y = find(u), find(v)
            if x==y:return 1
            
            if rank[x]<rank[y]:
                parent[x] = y
            elif rank[y]<rank[x]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x]+=1

            return 0
        tot = 0
        while pq:
            d,u,v = heappop(pq)
            if union(u,v):
                continue
            tot+=d
        return tot

class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(int)
        pq = []
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                heappush(pq,[abs(x1-x2) + abs(y1-y2),i,j])
                
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(u):
            if u==parent[u]:
                return u
            return find(parent[u])
        
        def union(u,v):
            x,y = find(u), find(v)
            if x==y:return 1
            
            if rank[x]<rank[y]:
                parent[x] = y
            elif rank[y]<rank[x]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x]+=1

            return 0
        tot = 0
        while pq:
            d,u,v = heappop(pq)
            if union(u,v):
                continue
            tot+=d
        return tot


        
        
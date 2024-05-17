from collections import *

inf = float('inf')
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append([v,w])
        k+=1
        dist = [inf]*n
        dist[src] = 0
        q = deque()
        q.append([0, src])
        while q and k>0:
            k-=1
            N = len(q)
            for _ in range(N):
                d, u = q.popleft()
                for v, w in adj[u]:
                    if d+w<dist[v]:  # using dist[u] + w will give you wrong answer
                        dist[v] = d+w
                        q.append([dist[v], v])
        return dist[dst] if dist[dst]!=float('inf') else -1


        
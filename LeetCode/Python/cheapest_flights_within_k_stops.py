class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append([v,w])
        dist = [float('inf')]*n
        dist[src] = 0
        q = deque()
        q.append([0,src])
        lvl = 0
        while lvl < k+1 and q:
            n = len(q)
            for _ in range(n):
                d,node = q.popleft()
                for v, w in adj[node]:
                    if d+w<dist[v]:
                        dist[v] = d+w
                        q.append([dist[v], v])

            lvl+=1
        
        x = dist[dst]
        return x if x!=float('inf') else -1
        
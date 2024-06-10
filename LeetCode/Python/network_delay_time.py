class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        q = []
        q.append([0,k])
        while q:
            di,u = heappop(q)
            if di>dist[u]:continue
            for v,w in adj[u]:
                if di+w<dist[v]:
                    dist[v] = di+w
                    heappush(q, [dist[v], v])
        x = max(dist[1:])
        if x==float('inf'):
            return -1
        return x
        
        
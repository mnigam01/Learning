class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                x, y = points[i]
                x2, y2 = points[j]
                dist = abs(x-x2) + abs(y-y2)
                heappush(pq,[dist,[i,j]])
        tot = 0
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(node):
            if node==parent[node]:
                return node
            return find(parent[node])
        def union(nodea, nodeb):
            parenta, parentb = find(nodea), find(nodeb)
            if parenta==parentb:
                return 1
            # rank_parenta, rank_parentb = 
            if rank[parenta]<rank[parentb]:
                parent[parenta] = parentb
            elif rank[parenta]>rank[parentb]:
                parent[parentb] = parenta
            else:
                parent[parentb] = parenta
                rank[parenta]+=1

            return 0
        
        while pq:
            d, [u,v] = heappop(pq)
            if union(u,v):
                continue
            else:
                tot += d
        return tot



        
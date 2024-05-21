class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(u):
            if u == parent[u]:
                return u
            return find(parent[u])
        def union(u,v):
            x,y = find(u), find(v)
            if x==y:
                return 1
            if rank[x]<rank[y]:
                parent[x] = y
            elif rank[y]<rank[x]:
                parent[y] = x
            else:
                parent[y] = x
                rank[y]+=1
            return 0
        
        for u, v in edges:
            union(u,v)
        
        return sum(i==v for i,v in enumerate(parent))


        
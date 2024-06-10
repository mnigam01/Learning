from heapq import heapify, heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        #  Method 1
        """res = [float('inf')]
        vis = set()
        def dfs(i,j,maxi = 0):
            if (i,j) in vis:
                return 
            maxi = max(maxi,grid[i][j])
            if maxi>res[0]:
                return 
            vis.add((i,j))
            if i==j==len(grid)-1:
                res[0] = min(res[0], maxi)

            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny = i+dx, j+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid):
                    dfs(nx,ny,maxi)
            vis.discard((i,j))
        
        dfs(0,0,0)
        return res[0]"""

        n = len(grid)

        # Method 2
        
        """def dfs(i,j,maxi):
            if grid[i][j]>maxi:
                return False
            if i==j==n-1:
                return True
            vis.add((i,j))
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in vis:
                    if dfs(nx,ny,maxi):
                        return True

            vis.discard((i,j))

            return False


        l,r = max(grid[0][0], grid[-1][-1]), n*n
        while l<r:
            m = (l+r)>>1
            vis = set()
            if dfs(0,0,m):
                r = m 
            else:
                l = m+1
        
        return l"""

        pq = []
        pq.append([grid[0][0], 0, 0])
        dist = [[float('inf')]*n for i in range(n)]
        dist[0][0] = grid[0][0]
        while pq:
            di,x,y = heappop(pq)
            if di>dist[x][y]:continue
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n:
                    if max(di,grid[nx][ny]) < dist[nx][ny]:
                        dist[nx][ny] = max(di,grid[nx][ny])
                        heappush(pq,[dist[nx][ny], nx, ny])
                    
        return dist[-1][-1]


        
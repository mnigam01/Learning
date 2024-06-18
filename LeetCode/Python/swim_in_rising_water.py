class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dist = [[float('inf')]*col for i in range(row)]
        pq = []
        heappush(pq, [grid[0][0], [0, 0]])
        dist[0][0] = grid[0][0]
        # seen = set()
        while pq:
            d, [x,y] = heappop(pq)
            if d>dist[x][y]:
                continue
            # seen.add((x,y))
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col :
                    if max(d, grid[nx][ny])<dist[nx][ny]:
                        dist[nx][ny] = max(d, grid[nx][ny])
                        heappush(pq, [dist[nx][ny], [nx,ny]])
        # print(dist)
        return dist[-1][-1]

            
# there is a binary search solution also but that is pretty slow
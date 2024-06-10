class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh+=1
        if fresh==0:
            return 0
        cnt = 0
        while q and fresh:
            cnt += 1
            N = len(q)
            for _ in range(N):
                x,y = q.popleft()
                for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        fresh-=1
                        q.append([nx,ny])
        if fresh>0:
            return -1
        return cnt


        
        
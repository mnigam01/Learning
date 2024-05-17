class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m  = len(board), len(board[0])

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!='O':
                return 
            board[i][j] = '#'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(n):
            for j in [0,m-1]:
                if board[i][j]=='O':
                    dfs(i,j)
        for j in range(m):
            for i in [0,n-1]:
                if board[i][j]=='O':
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j]=='#':
                    board[i][j] = 'O'


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])


        def dfs(i,j,ind):
            if ind==len(word):
                return True
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[ind]:
                return False
            tmp = board[i][j]
            board[i][j] = '.'
            for dx, dy in [[0, 1], [0,-1], [1,0], [-1,0]]:
                if dfs(i+dx,j+dy, ind+1):
                    return True
            board[i][j] = tmp
            return False



        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False





        
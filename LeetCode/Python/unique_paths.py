class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def h(i=0,j=0):
            if i==m-1 and j==n-1:
                return 1
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            return h(i+1,j)+h(i,j+1)
        
        return h()
        
from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    
        @cache
        def h(i=0,j=0):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if s[i]==t[j]:
                return h(i+1,j+1) + h(i+1,j)
            
            return h(i+1,j)
        
        return h(0,0)
        
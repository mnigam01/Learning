from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache 
        def h(i=0, j=0):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if i>=len(s):
                if j+1<len(p) and p[j+1]=='*':
                    return h(i,j+2)
                return False
            
            ans = False
            if s[i]==p[j] or p[j]=='.':
                ans |= h(i+1,j+1)
            
            if j+1<len(p) and p[j+1]=='*':
                ans |= h(i,j+2)
                if s[i]==p[j] or p[j]=='.':
                    ans |= h(i+1,j)
            return ans
        
        return h()
        
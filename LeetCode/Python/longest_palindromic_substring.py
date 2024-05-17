class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1,-1]
        length = 0
        n = len(s)
        def helper(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return [l+1, r-1]
        for i in range(n):
            l,r = helper(i,i)
            if r-l+1>length:
                length = r-l+1
                res = [l,r]
            if i+1<n:
                l,r = helper(i,i+1)
                if r-l+1>length:
                    length = r-l+1
                    res = [l,r]
        l,r = res
        return s[l:r+1]
            
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i<n-1:
                dp[i][i+1] = (s[i]==s[i+1])
        for length in range(3, n+1):
            for l in range(n-length+1):
                r = l+length-1
                dp[l][r] = ((s[l]==s[r]) and (dp[l+1][r-1]))
        return sum(sum(i) for i in dp)


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            left = right = i
            while left>=0 and right<n and s[left]==s[right]:
                ans += 1
                left-=1
                right+=1

            left, right = i, i+1
            while left>=0 and right<n and s[left]==s[right]:
                ans += 1
                left-=1
                right+=1
          
        return ans
        
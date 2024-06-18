from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def count(i = 0):
            if i>=len(s):
                return 1
            ans = 0
            if '1'<=s[i]<='9':
                ans += count(i+1)
            if i+1<len(s) and '10'<=s[i:i+2]<='26':  # if i don't write i+1 condition i get wrong answer
                ans += count(i+2)
            return ans
        return count()

            

        
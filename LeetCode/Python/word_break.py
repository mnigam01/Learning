from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def h(i=0):
            if i==len(s):
                return True
            for word in wordDict:
                if len(word)<=len(s)-i and (word==s[i:i+len(word)] and h(i+len(word))):
                    return True

            return False
        return h()




        
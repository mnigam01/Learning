from collections import *
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxi = 0
        l = 0
        d = defaultdict(int)
        for r,v in enumerate(s):
            d[v]+=1
            maxi = max(maxi,d[v])
            while r-l+1-maxi>k:
                # if d[s[l]]==maxi:
                #     maxi-=1
                d[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
            # print(res)

        return res
        
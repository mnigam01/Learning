class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = Counter(t)
        l = 0
        res = [-1,-1]
        d_s = defaultdict(int)
        cnt = 0
        length = float('inf')
        for r, v in enumerate(s):
            d_s[v]+=1
            if d_s[v]==d_t[v]:
                cnt+=1
            
            while cnt==len(d_t):
                if (r-l+1)<length:
                    length = r-l+1
                    res = [l,r]
                d_s[s[l]]-=1
                # if d_s[s[l]]==0:
                #     del d_s[s[l]]
                if d_s[s[l]]<d_t[s[l]]:
                    cnt-=1
                l+=1
        l,r = res
        return s[l:r+1] if length!=float('inf') else ""

                



        
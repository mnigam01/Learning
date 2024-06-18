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
    

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = Counter(t)
        sable = defaultdict(int)
        l = 0
        ans = [-1,-1]
        length = float('inf')
        tot = 0
        for r, v in enumerate(s):
            if v in table:
                sable[v]+=1
                if sable[v]==table[v]:
                    tot+=1
            while tot==len(table):
                if r-l+1<length:
                    length = r-l+1
                    ans = [l,r]
                if s[l] in table:
                    sable[s[l]]-=1
                    if sable[s[l]]<table[s[l]]:
                        tot-=1
                        # del sable[s[l]]
                l+=1
        l,r = ans
        return "" if length==float('inf') else s[l:r+1]
            



        
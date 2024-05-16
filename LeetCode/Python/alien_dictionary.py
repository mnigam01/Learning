from collections import *
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = defaultdict(int)  # this should be done here otherwise wrong answer
        for word in words:
            for ch in word:
                adj[ch] = []
                indegree[ch] = 0
        n = len(words)
        for i in range(1,n):
            a,b = words[i-1], words[i]
           
            flg = 1
            for j in range(min(len(a), len(b))):
                if a[j]!=b[j]:
                    adj[a[j]].append(b[j])
                    indegree[b[j]]+=1
                    flg = 0
                    break
            if flg and len(a)>len(b):
                return ""
        q = deque()
        for ch in indegree:
            if indegree[ch]==0:
                q.append(ch)

        res = ""
        while q:
            N = len(q)
            for _ in range(N):
                u = q.popleft()
                res+=u
                for v in adj[u]:
                    indegree[v]-=1
                    if indegree[v]==0:
                        q.append(v)
        
        return res if len(res)==len(adj) else ""

            

        
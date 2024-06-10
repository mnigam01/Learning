
[[Graph]]

Problem :- Alien Dictionary

mistakes i was doing in this problem
- using ascii_lowercase from string which contains more character which may not even present in alien_dict
- using two loop outer from (0,N) and inner from (i+1,N)
- not reversing from res string

1. Here to build adj in looking at b node and what is smaller than me goes to set. So if i'm the biggest element i'll not 0 indegree.

``` python

class Solution:
    def findOrder(self,alien_dict, N, K):
    
        adj = defaultdict(set)
        ascii_lowercase = set()  
        i = 0
        ascii_lowercase = ascii_lowercase.union(set(alien_dict[i]))
        for j in range(1,N):
            i = j-1
            if len(ascii_lowercase)<K:
                ascii_lowercase = ascii_lowercase.union(set(alien_dict[j]))
            
            mini = min(len(alien_dict[j]),len(alien_dict[i]))
            if len(alien_dict[j])<len(alien_dict[i]) and alien_dict[i][:mini]==alien_dict[j][:mini]:
                return ""
            self.helper(alien_dict[i],alien_dict[j],adj)
        indegree = defaultdict(int)
        for i in ascii_lowercase:
            for u in adj[i]:
                indegree[u]+=1
        
        res = ""
        q = deque([])
        for i in ascii_lowercase:
            if indegree[i]==0:
                q.append(i)
        while q:
            N = len(q)
            for _ in range(N):
                u = q.popleft()
                res+=u
                for v in adj[u]:
                    indegree[v]-=1
                    if indegree[v]==0:
                        q.append(v)
        
        return res[::-1] if len(res)==K else ""
        
        
    def helper(self,s,t,adj):
        for i in range(min(len(s),len(t))):
            if s[i]!=t[i]:
                adj[t[i]].add(s[i])
                return 

```

Problem :- Find cycle in a directed graph  (Course Schedule)
- Here normal dfs will fail (imagine graph as tree you start with node 1 and process all subtree and find no cycle, but later one of the parent of node 1 will say it is visited in past so there is cycle). For this you can use color property
- indegree
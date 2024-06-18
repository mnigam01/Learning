class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        for key in adj:
            adj[key].sort(reverse=True)
        src = "JFK"
        res = []
        stk = [src]
        while stk:
            src = stk[-1]
            if adj[src]:
                stk.append(adj[src].pop())
            else:
                res.append(stk.pop())

        return res[::-1]

        
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [[v,i] for i, v in enumerate(queries)]
        queries.sort()
        intervals.sort(key=lambda x:(x[0]))
        # print(intervals)
        # print(queries)
        res = [-1]*len(queries)
        pq = []
        ind = 0
        for v, i in queries:
            for j in range(ind,len(intervals)):
                if v<intervals[j][0]:
                    ind = j
                    break
                else:
                    start, end = intervals[j]
                    heappush(pq,[end-start+1, end])
            while pq and pq[0][1]<v:
                heappop(pq)
            
            if pq:
                res[i] = pq[0][0]


        return res
        
from sortedcontainers import SortedList
# from sortedcontainers import SortedList
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = SortedList([[v,i] for i,v in enumerate(queries)])
        # print(queries)
        intervals.sort(key=lambda x:(x[1]-x[0]))
        # print(intervals)
        ans = [-1]*len(queries)
        for l,r in intervals:
            while True:
                ind = bisect_left(queries,[l,])
                if ind<len(queries) and l<=queries[ind][0]<=r:
                    ans[queries[ind][1]] = r-l+1
                    queries.discard(queries[ind])
                else:
                    break

        return ans

        
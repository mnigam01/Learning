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
        
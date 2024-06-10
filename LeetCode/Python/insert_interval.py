class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            prv = newInterval
            res = []
            for i in range(len(intervals)):
                cur = intervals[i]
                if prv[1]<cur[0]:
                    res.append(prv[:])
                    prv = cur
                elif cur[1]<prv[0]:
                    res.append(cur[:])
                else:
                    prv = [min(prv[0], cur[0]), max(prv[1], cur[1])]
            res.append(prv[:])
            return res
        """

        # or sweep line
        intervals.append(newInterval)
        tmp = []
        for start, end in intervals:
            tmp.append([start,1])
            tmp.append([end,-1])
        tmp.sort(key=lambda x:(x[0], -x[1]))
        res = []
        tot = 0
        for point, delta in tmp:
            tot+=delta
            if tot==1 and delta==1:
                res.append([point,None])
            if tot==0 and delta==-1:
                res[-1][1] = point
        return res
        
        
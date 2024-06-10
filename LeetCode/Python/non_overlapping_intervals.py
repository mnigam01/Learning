class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        prv = -float('inf')
        cnt = 0
        for start, end in intervals:
            if prv<=start:
                # cnt+=1
                prv = end
            else:
                cnt+=1
            

        return cnt

        
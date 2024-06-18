class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1, max(bloomDay)
        def cond(mid):
            count = 0
            size = 0
            for i in bloomDay:
                if i<=mid:
                    size+=1
                    if size==k:
                        count+=1
                        size = 0
                else:
                    size = 0

                
                
            return count
                    
        while l<r:
            mid = (l+r)>>1
            if cond(mid)>=m:
                r = mid
            else:
                l = mid+1
        return l if cond(l)>=m else -1

        
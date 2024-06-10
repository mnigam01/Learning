class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l,r = 1, m*n

        def cond(mid):
            tot = 0
            print(m+1)
            for i in range(1,m+1):
                tot += mid//i
                # print(tot)
            print(l,r,mid,tot)
            return tot>=k


        while l<r:
            mid = (l+r)>>1
            if cond(mid):
                r = mid
            else:
                l = mid+1
        return l
        
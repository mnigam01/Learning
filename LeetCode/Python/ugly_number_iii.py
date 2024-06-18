class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l,r = min(a,b,c), a*n
        def cond(m):
            tot = m//a + m//b + m//c
            tot -= (m//lcm(a,b) + m//lcm(b,c)+ m//lcm(c,a))
            tot += (m//lcm(a,lcm(b,c)))
            # print(l,r,tot)
            return tot
        while l<r:
            m = (l+r)>>1
            if cond(m)>=n:
                r = m
            else:
                l = m+1
        return l
        
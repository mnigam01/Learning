class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = abs(n)
        
        def h(x, n):
            if n==0:
                return 1
            if n%2==0:
                return h(x,n//2)**2
            return x * h(x,n//2)**2
        
        return h(x,n)
        
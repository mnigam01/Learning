class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        """
        for i in range(20):
            x = 4**i
            if x==n:
                return True
            if x>n:
                break

        return False
        """

        """
        x = int(log(n)/log(4))
        # sometimes we may get wrong answer so using below if cond
        if 4**(x+1)==n:
            return True
        return 4**x==n
        """
        
        #for below approach see luluboy168
        return n&(n-1)==0 and n&1431655765!=0
        
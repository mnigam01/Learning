class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        """
        for i in range(20):
            x = 3**i
            if x==n:
                return True
            if x>n:
                break

        return False
        """

        """
        x = int(log(n)/log(3))
        # sometimes we may get wrong answer so using below if cond
        if 3**(x+1)==n:
            return True
        return 3**x==n
        """
        x = 3**20
        return x%n==0


        
        
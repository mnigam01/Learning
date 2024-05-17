class Solution:
    def reverse(self, x: int) -> int:
        flg = 0
        if x<0:
            flg = 1
            x = abs(x)
        
        ans = 0
        while x:
            ans = ans*10 + x%10
            x//=10
        
        ans = ans if not flg else -ans
        if not -(2**31)<=ans<(2**31):
            ans = 0
        
        return ans

        
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):   #in 32 bit number last number is 31 not 32 keep this in mind
            ans += ((n>>i)&1)*(1<<(31-i))
        return ans

        
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        # something similar to gray code
        res = [0,1]
        for i in range(1,n):
            N = len(res)
            for j in range(N-1,-1,-1):
                res.append((1<<i)+res[j])
        ind = res.index(start)
        return res[ind:] + res[:ind]

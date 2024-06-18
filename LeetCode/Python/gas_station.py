class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [i-j for i,j in zip(gas,cost)]
        if sum(delta)<0:
            return -1
        l = 0
        tot = 0
        for r in range(len(delta)):
            tot += delta[r]
            if tot<0:
                tot = 0
                l = r+1
        return l


        
        
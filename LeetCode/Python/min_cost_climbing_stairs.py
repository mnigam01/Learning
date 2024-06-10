class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def h(i):
            if i<0:
                return 0
            return min(h(i-1), h(i-2)) + cost[i]

        return min(h(n-1), h(n-2))
        
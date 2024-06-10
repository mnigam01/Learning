from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def h(target = amount):
            if target==0:
                return 0
            ans = float('inf')
            for coin in coins:
                if target>=coin:
                    ans = min(ans, h(target-coin))
            return ans + 1
        x = h() 
        return x if x!=float('inf') else -1

        
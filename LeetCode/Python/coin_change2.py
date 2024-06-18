from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        @cache
        def count_coins(i = 0, left = amount):
            if left==0:
                return 1
            if i>=len(coins):
                return 0
            ans = 0
            if coins[i]<=left:
                ans += count_coins(i, left-coins[i])
            j = i
            while j<len(coins) and coins[i]==coins[j]:
                j+=1
            ans += count_coins(j, left)
            return ans
        
        return count_coins()

        
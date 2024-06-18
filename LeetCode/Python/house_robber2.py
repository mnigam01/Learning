from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def maximize_profit(i = len(nums)-1, lastTaken=False):
            if i<0:
                return 0
                
            if i==0:
                return 0 if lastTaken else nums[0]
            ans = 0
            
            #take
            ans = max(ans, nums[i] + maximize_profit(i-2, lastTaken or i==len(nums)-1))

            #not take
            ans = max(ans, maximize_profit(i-1, lastTaken))

            return ans
               
                
        return maximize_profit()
        
from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def h(l=1, r=len(nums)-2):
            ans = 0
            for j in range(l,r+1):
                # bursting jth ballon
                ans = max(ans,h(l,j-1) + h(j+1,r) + nums[j]*nums[l-1]*nums[r+1])
            return ans
        
        return h()

        
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

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        @cache
        def h(i=1, j=len(nums)-2):
            # if i==j:return nums[i]   this is wrong consider the case of [1,5] -> [1,1,5,1] need to burst 1 first. with current i==j if i return 1 it'll be wrong instead i should return 5.
            if i>j:
                return 0
            ans = -float('inf')
            for k in range(i,j+1):
                ans = max(ans, h(i,k-1) + h(k+1,j) + nums[k]*nums[i-1]*nums[j+1])
            return ans
        return h()

        
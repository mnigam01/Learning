from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def h(i=n-1, lastUsed = False):
            if i<0:
                return 0
            if i==n-1:

                return max(nums[i] + h(i-2, True), h(i-1, lastUsed))
            elif i==0:
                if lastUsed:
                    return 0
                return max(nums[i] + h(i-2, lastUsed), h(i-1, lastUsed))
            return max(nums[i] + h(i-2, lastUsed), h(i-1, lastUsed))
        return h()
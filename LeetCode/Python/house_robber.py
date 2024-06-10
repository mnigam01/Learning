class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def h(i=len(nums)-1):
            if i<0:
                return 0
            return max(nums[i]+h(i-2), h(i-1))
        return h()
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        @cache
        def h(i = len(nums)-1, hasSold = False):
            if i<0:
                return -float('inf') if hasSold else 0
            if hasSold:
                return max(h(i-1, hasSold), -nums[i] + h(i-2, False))
            return max(h(i-1, hasSold), nums[i] + h(i-1, True ))
        
        return h()

        
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0, nums[-1]-nums[0]

        def cond(m):
            tot = 0
            for i, v in enumerate(nums):
                ind = bisect_right(nums, v+m)
                tot += (ind-i-1)
            # print(l,r,tot)
            return tot


        while l<r:
            m = (l+r)>>1
            if cond(m)>=k:
                r = m
            else:
                l = m+1
        return l
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        n = len(nums)
        l,r = 0, n-1

        def cond(m):
            if nums[l]<=nums[m]:
                if nums[l]<=nums[m]<=nums[r]:
                    return True
                return False
            else:
                return True


        while l<r:
            m = (l+r)>>1
            if cond(m):
                r = m
            else:
                l = m+1
        return nums[l]

        
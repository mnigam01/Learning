class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        def cond(m):
            if nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    return True
                return False
            else:
                if nums[m]<target<=nums[r]:
                    return False
                return True
        while l<r:
            m = (l+r)>>1
            if cond(m):
                r = m
            else:
                l = m+1
        return l if nums[l]==target else -1
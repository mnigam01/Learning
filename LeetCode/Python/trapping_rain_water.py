class Solution:
    def trap(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            l = r = i
            for j in range(i):
                if nums[j]>nums[l]:
                    l = j
            for j in range(i,N):
                if nums[j]>nums[r]:
                    r = j
            ans += min(nums[l], nums[r]) - nums[i]
        return ans

class Solution:
    def trap(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        stk = []
        for i in range(N):
            while stk and nums[stk[-1]]<nums[i]:
                ind = stk.pop()
                if stk:
                    h = min(nums[i],nums[stk[-1]])-nums[ind]
                    w = i-stk[-1]-1
                    ans += w*h
            stk.append(i)
        return ans

        
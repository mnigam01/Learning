class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1]*N 
        for i in range(1,N):
            res[i] = res[i-1]*nums[i-1]
        
        right = 1
        for i in range(N-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
        
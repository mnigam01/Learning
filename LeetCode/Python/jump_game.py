class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l,r = 0, nums[0]
        n = len(nums)
        while r<n-1 and l!=r:
            
            l,r = r, max(j+nums[j] for j in range(l,r+1))
        
        return r>=n-1

        
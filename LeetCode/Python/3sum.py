class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i,v in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k = i+1, n-1
            while j<k:
                tot = nums[i] + nums[j] + nums[k]
                if tot>0:
                    k-=1
                elif tot<0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
            


        return res
        
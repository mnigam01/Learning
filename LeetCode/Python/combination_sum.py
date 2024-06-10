class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()


        def helper(i = 0, target = target, cur = []):
            if target == 0:
                res.append(cur[:])
                return 
            if i>=len(nums):
                return 
            # take
            if nums[i]<=target:
                cur.append(nums[i])
                helper(i,target-nums[i],cur)
                cur.pop()
            
            #not take
            j = i
            while j<len(nums) and nums[i]==nums[j]:
                j+=1
            helper(j,target, cur)

        helper()
        return res
        
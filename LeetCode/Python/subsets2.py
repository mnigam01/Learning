class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def h(i=0, cur=[]):
            if i==len(nums):
                res.append(cur[:])
                return 
            cur.append(nums[i])
            h(i+1,cur)
            cur.pop()
            j = i
            while j<len(nums) and nums[i]==nums[j]:
                j+=1

            h(j,cur)
        
        h()

        return res
        
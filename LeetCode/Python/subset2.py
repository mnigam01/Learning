class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def h(i = 0, cur = []):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            h(i + 1, cur)
            cur.pop()
            j = i
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            h(j,cur)
        h()
        return res
        
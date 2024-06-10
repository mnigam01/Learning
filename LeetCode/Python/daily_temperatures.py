class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]<nums[j]:
        #             res[i] = j-i
        #             break
        # return res

        stk = []
        for i in range(n):
            while stk and nums[stk[-1]]<nums[i]:
                ind = stk.pop()
                res[ind] = i-ind
            stk.append(i)
        return res

        
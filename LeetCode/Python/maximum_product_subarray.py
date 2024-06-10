class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            ans = -float('inf')

            mini = maxi = 1
            for i in nums:
                mini,maxi = min(mini*i,maxi*i,i), max(mini*i,maxi*i,i)
                ans = max(ans,maxi,mini)


            return ans
        """
        ans = -float('inf')
        tot = 1
        tot2 = 1
        for i in range(len(nums)):
            tot*=nums[i]
            tot2*=nums[len(nums)-1-i]
            ans = max(ans,tot, tot2)
            if tot==0:
                tot = 1
            if tot2==0:
                tot2=1
        return ans

        
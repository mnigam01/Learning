class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {val:index for index, val in enumerate(s)}
        l = 0
        ans = []
        maxi = -1
        for r in range(len(s)):
            maxi = max(maxi,last_index[s[r]])
            if maxi==r:
                ans.append(r-l+1)
                l = r+1
                maxi = -1
            


        return ans

        
class Solution:
    def spiralOrder(self, nums: List[List[int]]) -> List[int]:
        n,m = len(nums), len(nums[0])
        top, bottom = 0, n-1
        left, right = 0, m-1
        res = []
        while left<=right and top<=bottom:
            for j in range(left,right+1):
                res.append(nums[top][j])
            top+=1

            for i in range(top,bottom+1):
                res.append(nums[i][right])
            right-=1

            if top<=bottom:
                for j in range(right, left-1, -1):
                    res.append(nums[bottom][j])
                bottom-=1


            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(nums[i][left])
                left+=1

        return res


        
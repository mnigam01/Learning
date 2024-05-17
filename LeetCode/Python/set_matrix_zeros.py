class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flg = 0
        n,m = len(nums), len(nums[0])
        for i in range(n):
            for j in range(m):
                if nums[i][j]==0:
                    if i==0:
                        flg = 1
                        nums[0][j] = 0
                    else:
                        nums[i][0] = 0
                        nums[0][j] = 0
        for j in range(1,m):
            if nums[0][j]==0:
                for i in range(1,n):
                    nums[i][j] = 0
        
        for i in range(1,n):
            if nums[i][0]==0:
                for j in range(1,m):
                    nums[i][j] = 0
        
        if nums[0][0]==0:
            for i in range(n):
                nums[i][0] = 0
        if flg:
            for j in range(m):
                nums[0][j] = 0



        
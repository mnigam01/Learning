class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Method 1
        """

            s = set()
            for i in nums:
                if i in s:
                    return i
                s.add(i)
            return -1
        
        """

        # Method 2
        slw = 0
        fst = 0
        while True:
            slw = nums[slw]
            fst = nums[nums[fst]]
            if slw == fst:
                break
        slw = 0
        while slw!=fst:
            slw = nums[slw]
            fst = nums[fst]
        return slw
        
        # Method 3
        """
            n = len(nums)
            for i in nums:
                nums[i%n]+=n
            for i in range(1,n):
                if nums[i]>2*n:
                    return i
            return 0
        """

        
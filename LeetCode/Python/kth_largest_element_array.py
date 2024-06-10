import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        
        # heapify(nums)
        # while len(nums)>k:
        #     heappop(nums)
        
        # return nums[0]


        # quickselect algorithm and worst time complexity is n2

        val = random.choice(nums)
        greater = []
        equal = []
        smaller = []
        for v in nums:
            if v>val:
                greater.append(v)
            elif v<val:
                smaller.append(v)
            else:
                equal.append(v)
        
        if len(greater)>=k:
            return self.findKthLargest(greater, k)
        elif len(greater) + len(equal)>=k:
            return equal[0]
        else:
            return self.findKthLargest(smaller, k - len(greater) - len(equal))
        
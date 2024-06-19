class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        stk = [-1]
        nums.append(-1)
        ans = 0
        for i, v  in enumerate(nums):
            # print(stk)
            while len(stk)>1 and nums[stk[-1]]>v:
                ind = stk.pop()
                if stk:
                    w = i-stk[-1]-1
                    h = nums[ind]

                    ans = max(ans,h*w)
            stk.append(i)

        return ans

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        ans = 0
        stk = [-1]
        for i in range(len(heights)):
            while stk and heights[stk[-1]]>heights[i]:
                
                ind = stk.pop()
                
                w = i-stk[-1]-1
                h = heights[ind]
                ans = max(ans,w*h)
            stk.append(i)
        return ans


        
        
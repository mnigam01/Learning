class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        
        heappush(self.left, -num)

        if len(self.left)-len(self.right)>0:
            # if len(self.right):

            heappush(self.right, -heappop(self.left))
        
        if len(self.left) and len(self.right) and -self.left[0]>self.right[0]:

            heappush(self.right, -heappop(self.left))
            heappush(self.left, -heappop(self.right))
        
        

    def findMedian(self) -> float:
        
        n =  len(self.left)+ len(self.right)
        if n&1:
            return self.right[0]
        return (-self.left[0] + self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
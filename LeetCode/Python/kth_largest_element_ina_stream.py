from heapq import heapify, heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums[:]
        self.k = k
        heapify(self.pq)
        while len(self.pq)>self.k:
            heappop(self.pq)

        

    def add(self, val: int) -> int:
        heappush(self.pq,val)
        while len(self.pq)>self.k:
            heappop(self.pq)
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
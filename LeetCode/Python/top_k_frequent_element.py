class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        # Method 1
        """
            tmp = [i for i,j in sorted(d.items(), key=lambda x:-x[1])]
            return tmp[:k]
        """

        # Method 2

        """
            pq = []
            for key, val in d.items():
                heappush(pq,[val,key])
                # print(pq)
                while len(pq)>k:
                    heappop(pq)
            tmp = [key for cnt,key in pq]
            return tmp
        """

        # Method 3 bucket sort
        buckets = [[] for i in range(len(nums)+1)]
        for key, val in d.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for element in buckets[i]:
                res.append(element)
                if len(res)==k:
                    return res

        return res


        
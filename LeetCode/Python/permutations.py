class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = set(nums)

        def h(cur = []):
            if len(cur) ==len(nums):
                res.append(cur[:])
                return
            tmp = counter.copy()
            for key in tmp:
                
                counter.discard(key)
                cur.append(key)
                h()
                cur.pop()
                counter.add(key)
                # counter[key]+=1

        h()

        return res
        
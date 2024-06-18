class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def create_combinations(ind = 0, remaining_target=target, cur =[]):
            if remaining_target==0:
                res.append(cur[:])
                return
            if ind>=len(candidates):
                return
            if candidates[ind]<=remaining_target:
                cur.append(candidates[ind])
                create_combinations(ind+1, remaining_target-candidates[ind], cur)
                cur.pop()
            j = ind
            while j<len(candidates) and candidates[j]==candidates[ind]:
                j+=1
            create_combinations(j, remaining_target, cur)


        create_combinations()
        return res
        
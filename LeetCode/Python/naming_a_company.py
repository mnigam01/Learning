class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        for idea in ideas:
            d[idea[0]].add(idea[1:])
        
        ans = 0
        keys = list(d.keys())
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                set_a = d[keys[i]]
                set_b = d[keys[j]]
                l = len(set_a.intersection(set_b))
                ans += 2*((len(set_a)-l)*(len(set_b)-l))
        return ans

        
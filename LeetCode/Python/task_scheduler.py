from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        maxi = max(d.values())
        empty_slots = (maxi-1)*(n+1)
        for key, value in d.items():
            empty_slots -= min(value, maxi-1)
        
        if empty_slots<0:
            return len(tasks)
        return len(tasks) + empty_slots

        
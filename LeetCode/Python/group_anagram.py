class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        d = defaultdict(list)
        for word in strs:
            d[''.join(sorted(word))].append(word)

        return d.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        d = defaultdict(list)
        for word in strs:
            d[tuple(sorted(word))].append(word)

        return d.values()
        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        d = defaultdict(list)
        for word in strs:
            tmp = [0]*26
            for ch in word:
                tmp[ord(ch)-ord('a')]+=1
            d[tuple(tmp)].append(word)

        return d.values()
        
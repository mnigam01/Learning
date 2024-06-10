class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def h(i=0):
            if i==len(s):
                return [[]]
            res = []
            for j in range(i,len(s)):
                if check(i,j):
                    tmp = h(j+1)
                    for element in tmp:
                        res.append([s[i:j+1]]+element)
            return res
        
        return h()

        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        res = []
        if len(digits)==0:
            return []
        def h(i=0,cur=""):
            if i==len(digits):
                res.append(cur)
                return 
            for ch in d[int(digits[i])]:
                h(i+1,cur+ch)
        h()
        return res
        
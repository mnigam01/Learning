class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        res = []
        def h(i=0, cur=""):
            if i==len(digits):
                res.append(cur)
                return
            for v in d[digits[i]]:
                h(i+1,cur+v)
        if digits=="":
            return []
        h()
        return res
        
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i not in d:
                stk.append(i)
            else:
                if not stk or stk[-1]!=d[i]:
                    return False
                stk.pop()
        return len(stk)==0

        
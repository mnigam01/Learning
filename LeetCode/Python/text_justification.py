class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        tmp = []
        word = 0
        for i in words:
            if word + len(tmp) + len(i)>maxWidth:
                space_remaining = maxWidth- word
                n = max(1, len(tmp)-1)
                for j in range(space_remaining):
                    tmp[j%n] += ' '
                res.append(''.join(tmp)) 
                tmp = []
                word = 0
            tmp.append(i)
            word+=len(i)
        
        tmp = ' '.join(tmp)
        tmp = tmp.ljust(maxWidth,' ')
        res.append(tmp)




        return res
        
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res+=str(len(word))+'#'+word
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i<len(s):
            l = ''
            while i<len(s) and s[i]!='#':
                l+=s[i]
                i+=1
            i+=1
            l = int(l)
            res.append(s[i:i+l])
            i+=l

        return res

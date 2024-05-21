class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Method 1
        """
            res = [0]
            s = set([0])
            def h():
                if len(res)==(1<<n):
                    return True
                last = res[-1]
                for i in range(n):
                    val = last^(1<<i)
                    if val not in s:
                        s.add(val)
                        res.append(val)
                        if h():
                            return True
                        s.discard(val)
                        res.pop()
                return False
            h()
            return res
        """
    
   
        res = [0,1]
        def h(i=1):
            if len(res)==(1<<n):
                return 
            N = len(res)
            res.extend(res[::-1])
            for j in range(N,len(res)):
                res[j] = (1<<i)+res[j]
            h(i+1)

        h()
        return res

        
class Solution:
    def checkValidString(self, s: str) -> bool:
        # @cache
        # def h(i = 0, tot = 0):
        #     if i==len(s):
        #         return tot==0
        #     if tot<0:
        #         return False
        #     if s[i]=='(':
        #         return h(i+1,tot+1)
        #     elif s[i]==')':
        #         return h(i+1,tot-1)
        #     else:
        #         return h(i+1,tot+1) or h(i+1,tot-1) or h(i+1,tot)
        
        # return h()

        mini,maxi = 0, 0
        for i in s:
            if i=='(':
                mini+=1
                maxi+=1
            elif i==')':
                mini-=1
                maxi-=1
            else:
                mini-=1
                maxi+=1
            
            if maxi<0:
                return False
            mini = max(mini,0)
        return mini==0

        
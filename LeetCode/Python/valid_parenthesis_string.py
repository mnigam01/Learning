class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def h(i=0, tot=0):
            if tot<0:   # this statement is important here ")))(((" consider this example without this
                return False
            if i==len(s):
                return tot==0
            if s[i]=='(':
                return h(i+1,tot+1)
            elif s[i]==')':
                return h(i+1,tot-1)
            return h(i+1,tot+1) or h(i+1,tot-1) or h(i+1,tot)
        
        return h()
        

class Solution:
    def checkValidString(self, s: str) -> bool:

        mini = maxi = 0
        for i in s:
            if i=='(':
                maxi += 1
                mini += 1
            elif i==')':
                maxi-=1
                mini-=1
            else:
                maxi+=1
                mini-=1
            if maxi<0:
                return False
            mini = max(mini,0)
        return mini==0

"""
maxi is maximum number of open bracket if i is open bracket it will increase
mini is minimum numberr of open bracket if i is open bracket it will increase

maxi will decrease if i is close bracket
mini will decrease if i is close bracket

maxi will increase if i is * bcz will consider is open bracket
mini will decrease if i is * bcz will consider is close bracket

if maxi becomes 0 it means even after considering all * and open bracket combined we can't overcome close bracket return false
if mini is negative it means * + close bracket are more so will convert some * to open bracket. 

in last just check if mini is 0 or not  consider ((() this example
basically if mini is >0 means there are more open brackets in expression
"""
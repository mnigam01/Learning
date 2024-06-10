class Solution:
	def idToShortURL(self,n):
		# code here
		store = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		res = []
		while n:
		    res.append(n%62)
		    n//=62
        res = res[::-1]
        ans = ""
        for i in res:
            ans += store[i]
        return ans
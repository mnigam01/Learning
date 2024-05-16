# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(cur = root, maxi = -float('inf')):
            if not cur:
                return 
            if cur.val>=maxi:
                maxi = cur.val
                res[0]+=1
            dfs(cur.left,maxi)
            dfs(cur.right,maxi)
        dfs()
        return res[0]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def h(root=root,mini=-float('inf'), maxi=float('inf')):
            if not root:
                return True
            if not (mini<root.val<maxi):
                return False
            return h(root.left,mini,root.val) and h(root.right,root.val,maxi)
        return h()
        
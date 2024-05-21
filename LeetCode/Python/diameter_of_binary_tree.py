# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def h(root=root):
            if not root:
                return 0
            left = h(root.left) if root.left else -1
            right = h(root.right) if root.right else -1
            res[0] = max(res[0], left+right+2)
            return 1 + max(left,right)
        h(root)
        return res[0]
        
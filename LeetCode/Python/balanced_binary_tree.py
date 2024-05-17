# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left==float('inf') or right==float('inf') or abs(left-right)>1:
                return float('inf')
            return 1 + max(left,right)

        ans = helper(root)
        return ans != float('inf')
        
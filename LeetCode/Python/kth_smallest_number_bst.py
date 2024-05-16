# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Method 1
        """
            res = []
            def inorder(cur=root):
                if not cur:return
                inorder(cur.left)
                res.append(cur.val)
                inorder(cur.right)
            inorder()
            return res[k-1]
        """

        # Method 2
        cnt = 0
        cur = root
        stk = []
        while stk or cur:
            if cur:
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                cnt+=1
                if cnt==k:
                    return cur.val
                cur = cur.right
        return -1
        
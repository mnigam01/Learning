# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            cur = []
            N = len(q)
            for _ in range(N):
                u = q.popleft()
                cur.append(u.val)
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            res.append(cur)
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = defaultdict(int)
        for i,v in enumerate(inorder):
            d[v] = i
        res = [0]
        def h(l=0,r=len(preorder)-1):
            if l>r:
                return None
            val = preorder[res[0]]
            node = TreeNode(val)
            res[0]+=1
            node.left = h(l,d[val]-1)
            node.right = h(d[val]+1,r)
            return node
        return h()
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = defaultdict(int)
        for i,v in enumerate(inorder):
            d[v] = i
        res = [0]
        def h(l=0,r=len(preorder)-1):
            if l==r:    
                tmp = TreeNode(inorder[l])
                res[0] += 1
                return tmp
            if l>r:
                return None
            val = preorder[res[0]]
            node = TreeNode(val)
            res[0]+=1
            node.left = h(l,d[val]-1)
            node.right = h(d[val]+1,r)
            return node
        return h()
        
        
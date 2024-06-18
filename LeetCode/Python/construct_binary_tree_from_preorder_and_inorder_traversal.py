# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_mapping = {}
        for ind,val in enumerate(inorder):
            index_mapping[val] = ind
        ind = [0]

        def build(left=0, right=len(inorder)-1):
            if left>right:
                return None
            if left==right:
                ind[0]+=1
                return TreeNode(inorder[left])
            mid = index_mapping[preorder[ind[0]]]
            node = TreeNode(preorder[ind[0]])
            ind[0]+=1
            left = build(left,mid-1)
            right = build(mid+1,right)
            node.left = left
            node.right = right


            return node
        return build()
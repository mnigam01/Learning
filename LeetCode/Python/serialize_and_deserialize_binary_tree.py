# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # res = ""
        def h(root):
            if not root:
                return '#'
            return str(root.val) + '.' + h(root.left) + '.' +h(root.right)
            
        return h(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split('.')
        ind = [0]
        def h():
            if ind[0]>=len(data):
                return None
            if data[ind[0]]=='#':
                ind[0]+=1
                return None
            root = TreeNode(int(data[ind[0]]))
            ind[0]+=1
            root.left = h()
            root.right = h()
            return root
        return h()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
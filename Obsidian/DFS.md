[[Tree]]  Time complexity :- n   Space Complexity :- n
```python

class Solution:

    # Some function to return inorder Traversal -> Given is root node

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        inorder = []
        self.helper(root,inorder)
        return inorder

    def helper(self,root,inorder):

        if not root:
            return

        self.helper(root.left,inorder)
        inorder.append(root.val)
        self.helper(root.right,inorder)

```

in recursive we use stack or need to get the latest node in data that's why we are going to use stack here.

iterative version

``` python

class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stk = []
        
        while stk or root:
            if root:
                res.append(root.val)
                stk.append(root)
                root = root.right
            else:
                root = stk.pop()
                root = root.left

        res.reverse()

        return res
        
```


``` python
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stk = []

        while stk or root:

            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                res.append(root.val)
                root = root.right

  

        return res
```

``` python

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

  
        stk = []
        res = []

        while root or stk:

            if root:
                res.append(root.val)
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                root = root.right

        return res

```


min/max depth

``` python
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1+self.minDepth(root.right)

        if not root.right:
            return 1+self.minDepth(root.left)

        return 1+ min(self.minDepth(root.left), self.minDepth(root.right))

```

same tree
``` python

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if (not p)^(not q):
            return False

        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

```

symmetric tree

``` python
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,root)

    def helper(self,p,q):
        if not p and not q:return True
        if (not p)^(not q):return False

        return p.val==q.val and self.helper(p.left,q.right) and self.helper(p.right,q.left)
```

height balanced tree  O(n)

``` python
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        x = self.helper(root)
        return x>=0

    def helper(self,root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        x = self.helper(root.left)
        y = self.helper(root.right)
        if x==-1 or y==-1 or abs(x-y)>1:
            return -1

        return 1+max(x,y)
```

O(n2)
``` python
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        x = self.helper(root.left)
        y = self.helper(root.right)
        return abs(x-y)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        x = self.helper(root.left)
        y = self.helper(root.right)
        return 1+max(x,y)
```
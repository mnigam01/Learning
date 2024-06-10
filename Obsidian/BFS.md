[[Tree]]        Time complexity :- n   Space Complexity :- n
``` python

from collections import deque

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        queue = deque([root])
        level_order_list = []
        
        while len(queue):
            N = len(queue)
            
            for i in range(N):
                node = queue.popleft()
                level_order_list.append(node.data)
                
                for children in [node.left,node.right]:
                    if children:
                        queue.append(children)
                        
        return level_order_list

```

zig zag traversal (both insertion + how you insert children in flg is important)

``` python
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        level_order_list = []
        flg = 1
        while len(queue):
            N = len(queue)
            tmp = []
            for i in range(N):
                if flg:
                    node = queue.popleft()
                else:
                    node = queue.pop()
                tmp.append(node.val)
                if flg:
                    for children in [node.left,node.right]:
                        if children:
                            queue.append(children)
                else:
                    for children in [node.right,node.left]:
                        if children:
                            queue.appendleft(children)
            flg ^= 1
            level_order_list.append(tmp)

        return level_order_list
```

find bottom left value 

``` python
class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        #method 1 using bfs

        queue = deque([root])
        while len(queue):
            level_order_list = []
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                level_order_list.append(node.val)
                for children in [node.left,node.right]:
                    if children:
                        queue.append(children)
        return level_order_list[0]

```

another variant [[DFS]]

``` python

class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
  
        #method 2 using dfs
        res = []
        self.dfs(root,0,res)
        return res[-1]

    def dfs(self,root,level,res):
        if not root:
            return
        if len(res)==level:
            res.append(root.val)
        self.dfs(root.left,level+1,res)
        self.dfs(root.right,level+1,res)
```

Right view of tree [[DFS]]

``` python

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        self.helper(root,0,res)
        return res
    
    def helper(self,root,lvl,res):
        if not root:
            return 

        if len(res)==lvl:
            res.append(root.val)

        self.helper(root.right,lvl+1,res)
        self.helper(root.left,lvl+1,res)

```

``` python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        q = deque([root])
        cnt = 0
        while q:
            N = len(q)
            for _ in range(N):
                u = q.popleft()
                if len(res)==cnt:
                    res.append(u.val)
                # here i'm doing right and left to prevent again and again overwriting again we could have done that also.
                for v in [u.right,u.left]:
                    if v:
                        q.append(v)

            cnt += 1
        return res
    
```

bottom view (more difficult than previous views)  [[DFS]]   (here we are interested in right if collision)
``` python

from collections import defaultdict
class Solution:
    def bottomView(self, root):
        # code here
        d = defaultdict(int)
        self.dfs(root,0,0,d)
        items = sorted([[key,value[0]] for key,value in d.items()])
        return [j for i,j in items]
        
        
    def dfs(self,root,ver,hor,d):
        if not root:
            return 
        if (ver not in d) or hor>=d[ver][1]:
            d[ver] = [root.data,hor]
        self.dfs(root.left,ver-1,hor+1,d)
        self.dfs(root.right,ver+1,hor+1,d)

```

other variant 

``` python
from collections import defaultdict, deque
class Solution:
    def bottomView(self, root):
        # code here
        d = defaultdict(int)
        q = deque([[root,0,0]])  #ver,hor
        while q:
            N = len(q)
            for i in range(N):
                u,ver,hor = q.popleft()
                if ver not in d or hor>=d[ver][1]:
                    d[ver] = [u.data,hor]
                if u.left:
                    q.append([u.left,ver-1,hor+1])
                if u.right:
                    q.append([u.right,ver+1,hor+1])
                
        
        
        items = sorted([[key,value[0]] for key,value in d.items()])
        return [j for i,j in items]
```

top view  (here we are interested in left if collision)

``` python

from collections import defaultdict, deque

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        d = defaultdict(int)
        self.dfs(root,0,0,d)
        item = sorted([[key,value[0]] for key, value in d.items()])
        return [j for i,j in item]
    
    def dfs(self,root,ver,hor,d):
        if not root:
            return 
        if ver not in d or hor<d[ver][1]:
            d[ver] = [root.data,hor]
        self.dfs(root.left,ver-1,hor+1,d)
        self.dfs(root.right,ver+1,hor+1,d)
        
```

other variant

``` python
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        d = defaultdict(int)
        q = deque([[root,0,0]])
        while q:
            N = len(q)
            for _ in range(N):
                u,ver,hor = q.popleft()
                if ver not in d or hor<d[ver][1]:
                    d[ver] = [u.data,hor]
                if u.left:
                    q.append([u.left,ver-1,hor+1])
                if u.right:
                    q.append([u.right,ver+1,hor+1])
                    
        
        item = sorted([[key,value[0]] for key, value in d.items()])
        return [j for i,j in item]

```

good problem on getting only the boundary of tree starting from left and below and then right
idea is to first add root, then dfs on left ignoring the left extreme leaf node. then search for leaf node in left subtree and then then search for leaf node in right subtree and then do dfs on right subtree add data in reverse order.
``` python

class Solution:
    def printBoundaryView(self, root):
        if not root:
            return []
        # Code here
        res = []
        
		res.append(root.data)
        self.dfs(root.left,res)
        
        self.dfs2(root.left,res)
        self.dfs2(root.right,res)
        
        self.dfs3(root.right,res)
        return res
        
    def dfs(self,root,res):
        if not root:
            return
        if not root.left and not root.right:
            return 
        
        res.append(root.data)
        if root.left:
            self.dfs(root.left,res)
        else:
            self.dfs(root.right,res)
        
    def dfs2(self,root,res):
        if not root:
            return 
        if not root.left and not root.right:
            res.append(root.data)
            return
        self.dfs2(root.left,res)
        self.dfs2(root.right,res)
        
    def dfs3(self,root,res):
        if not root:
            return 
        if not root.left and not root.right:
            return 
        
        if root.right:
            self.dfs3(root.right,res)
        else:
            self.dfs3(root.left,res)
        res.append(root.data)
```
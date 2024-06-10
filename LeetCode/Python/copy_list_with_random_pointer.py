"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        # def h(cur = head):
        #     if not cur:
        #         return cur
        #     if cur in d:
        #         return d[cur]
        #     new_node = Node(cur.val)
        #     d[cur] = new_node
        #     new_node.next = h(cur.next)
        #     new_node.random = h(cur.random)
        #     return new_node
        
        # return h()

        d = {None:None}

        dummy = Node(-1)
        prv = dummy
        cur = head
        while cur:
            new_node = Node(cur.val)
            d[cur] = new_node
            prv.next = new_node
            prv = new_node
            cur = cur.next
        
        cur = head
        while cur:
            d[cur].random = d[cur.random]
            cur = cur.next

        return dummy.next
       
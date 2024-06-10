# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tmp = head
        for i in range(k):
            if not tmp:
                return head
            tmp = tmp.next
        #reverse 
        newHead = self.reverseK(head,k)
        head.next = self.reverseKGroup(tmp,k)
        return newHead




    def reverseK(self,root,k):
        cnt = 0
        prv = None
        while root and cnt<k:
            tmp = root.next
            root.next = prv
            prv = root
            root = tmp
            cnt+=1
        return prv
        
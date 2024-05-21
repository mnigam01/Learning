# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        dummy = ListNode(next=head)
        slw = dummy
        fst = dummy
        while fst and fst.next:
            slw = slw.next
            fst = fst.next.next
        
        cur = slw.next
        slw.next = None
        prv = None
        while cur:
            tmp = cur.next
            cur.next = prv
            prv = cur
            cur = tmp
        
        l1 = dummy.next
        l2 = prv
        prv = dummy
        flg = 1
        while l1 and l2:
            if flg:
                prv.next = l1
                l1 = l1.next
            else:
                prv.next = l2
                l2 = l2.next
            flg ^=1
            prv = prv.next
        if l1:
            prv.next = l1
        if l2:
            prv.next = l2
        return dummy.next

        
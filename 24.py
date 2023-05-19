# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head
        
        if not head.next.next:
            p0 = head.next
            head.next.next = head
            head.next = None
            return p0

        p0 = head
        p1 = head.next
    
        p0.next = p1.next
        p1.next = p0

        _head = p1

        p1 = p1.next.next

        while p1:
            if not p1.next:
                return _head

            p0.next = p1.next
            p1.next = p1.next.next
            p0.next.next = p1
            p1 = p1.next
            p0 = p0.next.next

        return _head

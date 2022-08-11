# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        if not head.next.next:
            return head.next
        
        curr = head.next
        middle = head.next
        
        epoch = 0
        
        while curr.next:
            curr = curr.next
            epoch += 1
            if epoch == 2:
                middle = middle.next
                epoch = 0
                
        return middle
            

from imports import *

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        
        temp = result
        for _ in range(n):
            head = head.next
        
        while head:
            temp = temp.next
            head = head.next
        
        temp.next = temp.next.next
        
        return result.next

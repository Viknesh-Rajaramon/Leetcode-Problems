from imports import *

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        
        if n == 0 or k == 0:
            return head

        k = k % n

        ptr1, ptr2 = head, head
        while ptr1.next and k > 0:
            ptr1 = ptr1.next
            k -= 1

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = head
        head = ptr2.next
        ptr2.next = None
        return head

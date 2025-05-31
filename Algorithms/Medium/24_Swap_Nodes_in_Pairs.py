from imports import *

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        result = ListNode(0)
        result.next = head

        ptr1, ptr2 = result, head
        while ptr2 and ptr2.next:
            temp = ptr2.next
            ptr2.next = temp.next
            ptr1.next = temp
            temp.next = ptr2
            ptr1 = ptr2
            ptr2 = ptr2.next

        return result.next

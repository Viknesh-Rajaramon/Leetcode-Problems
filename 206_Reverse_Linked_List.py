from imports import *

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = None
        while head is not None:
            temp = ListNode(val=head.val, next=reverse_head)
            reverse_head = temp
            head = head.next

        return reverse_head

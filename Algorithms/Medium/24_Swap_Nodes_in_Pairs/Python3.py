from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

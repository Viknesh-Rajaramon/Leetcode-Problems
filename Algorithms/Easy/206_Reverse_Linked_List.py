from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = None
        while head is not None:
            temp = ListNode(val=head.val, next=reverse_head)
            reverse_head = temp
            head = head.next

        return reverse_head

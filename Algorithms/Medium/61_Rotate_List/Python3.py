from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n, ptr, tail = 0, head, None
        while ptr:
            tail, ptr = ptr, ptr.next
            n += 1

        k, tail.next, result = k%n, head, None
        while n-k != 0:
            result, head = head, head.next
            n -= 1
        
        result.next = None
        return head

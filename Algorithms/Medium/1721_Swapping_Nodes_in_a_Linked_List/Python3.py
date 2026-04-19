from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k-1):
            curr = curr.next
        
        k_node_begin = curr
        k_node_end = head
        while curr.next:
            k_node_end = k_node_end.next
            curr = curr.next
        
        k_node_begin.val, k_node_end.val = k_node_end.val, k_node_begin.val
        return head

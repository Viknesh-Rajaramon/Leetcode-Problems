from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s_list, b_list = ListNode(), ListNode()
        small, big = s_list, b_list

        while head:
            if head.val < x:
                small.next, small = head, head
            else:
                big.next, big = head, head
            
            head = head.next
        
        big.next = None
        small.next = b_list.next

        return s_list.next

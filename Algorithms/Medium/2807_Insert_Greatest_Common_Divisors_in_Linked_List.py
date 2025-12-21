from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head
        next_node = head.next

        while next_node is not None:
            gcd_val = gcd(prev_node.val, next_node.val)
            new_node = ListNode(gcd_val, next_node)
            prev_node.next = new_node
            prev_node = next_node
            next_node = next_node.next
        
        return head

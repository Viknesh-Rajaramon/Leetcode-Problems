from imports import *

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head
        next_node = head.next

        sum_ = 0
        
        while next_node is not None:
            if next_node.val != 0:
                sum_ += next_node.val
                next_node = next_node.next
            else:
                prev_node = prev_node.next
                prev_node.val = sum_
                prev_node.next = next_node
                next_node = next_node.next
                sum_ = 0
        
        head = head.next
        prev_node.next = None

        return head

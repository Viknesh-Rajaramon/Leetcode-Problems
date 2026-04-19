from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_map = [head]
        pointer = head
        
        while pointer is not None:
            pointer = pointer.next
            
            if pointer in visited_map:
                return True
            
            visited_map.append(pointer)
        
        return False

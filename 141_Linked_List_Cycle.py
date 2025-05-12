from imports import *

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

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if head.next is None:
            return [0]
        
        curr_ptr = head
        
        answers = []
        while curr_ptr is not None:
            next_max = 0
            next_ptr = curr_ptr.next
            while next_ptr is not None:
                if next_ptr.val > curr_ptr.val:
                    next_max = next_ptr.val
                    break
                
                next_ptr = next_ptr.next
            
            answers.append(next_max)
            curr_ptr = curr_ptr.next
        
        return answers

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()

        ptrA = headA
        while ptrA:
            s.add(ptrA)
            ptrA = ptrA.next
        
        ptrB = headB
        while ptrB:
            if ptrB in s:
                return ptrB
                
            ptrB = ptrB.next

        return None

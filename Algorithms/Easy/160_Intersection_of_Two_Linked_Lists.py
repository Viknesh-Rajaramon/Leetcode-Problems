from imports import *

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

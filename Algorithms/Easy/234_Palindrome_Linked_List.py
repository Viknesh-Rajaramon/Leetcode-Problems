from imports import *

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev
        
        first, second = head, reverse_linked_list(slow)
        while first and second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True

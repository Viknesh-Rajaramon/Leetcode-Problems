from imports import *

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums, dummy = set(nums), ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next

        return dummy.next

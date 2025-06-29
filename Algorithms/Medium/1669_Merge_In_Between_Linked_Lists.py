from imports import *

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr1 = list1
        for _ in range(a-1):
            ptr1 = ptr1.next

        ptr2 = list1
        for _ in range(b+1):
            ptr2 = ptr2.next
        
        ptr1.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = ptr2
        return list1

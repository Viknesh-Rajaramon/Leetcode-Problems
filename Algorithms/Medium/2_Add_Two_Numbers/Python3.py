from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumListNode = ListNode()
        pointer = sumListNode
        carry = 0

        i, j = l1, l2

        while i is not None and j is not None:
            sum = (i.val + j.val + carry) % 10
            carry = (i.val + j.val + carry) // 10
            temp = ListNode(sum)
            pointer.next = temp
            pointer = pointer.next
            i = i.next
            j = j.next
        
        while i is not None:
            sum = (i.val + carry) % 10
            carry = (i.val + carry) // 10
            temp = ListNode(sum)
            pointer.next = temp
            pointer = pointer.next
            i = i.next
        
        while j is not None:
            sum = (j.val + carry) % 10
            carry = (j.val + carry) // 10
            temp = ListNode(sum)
            pointer.next = temp
            pointer = pointer.next
            j = j.next
        
        if carry != 0:
            temp = ListNode(carry)
            pointer.next = temp

        sumListNode = sumListNode.next
        return sumListNode

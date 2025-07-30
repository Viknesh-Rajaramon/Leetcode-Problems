from imports import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next

        num2 = []
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None
        while num1 and num2:
            num = num1.pop() + num2.pop() + carry
            carry = num // 10
            new_node = ListNode(num % 10)
            new_node.next = head
            head = new_node
        
        while num1:
            num = num1.pop() + carry
            carry = num // 10
            new_node = ListNode(num % 10)
            new_node.next = head
            head = new_node
        
        while num2:
            num = num2.pop() + carry
            carry = num // 10
            new_node = ListNode(num % 10)
            new_node.next = head
            head = new_node
        
        if carry:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node
        
        return head

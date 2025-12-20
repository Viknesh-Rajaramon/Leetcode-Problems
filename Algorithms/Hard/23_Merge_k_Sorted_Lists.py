from typing import Optional, List
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        heap = []
        
        ptrs = [None] * n
        for i in range(n):
            if lists[i]:
                ptrs[i] = lists[i]
                heappush(heap, (ptrs[i].val, i))
        
        result, ptr = None, None
        while heap:
            val, index = heappop(heap)
            if not result:
                result = ListNode(val)
                ptr = result
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next
            
            if ptrs[index].next:
                ptrs[index] = ptrs[index].next
                heappush(heap, (ptrs[index].val, index))

        return result

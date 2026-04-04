from typing import Optional, List
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n, min_heap = len(lists), []
        ptrs = [None] * n
        for i in range(n):
            if lists[i]:
                ptrs[i] = lists[i]
                min_heap.append((ptrs[i].val, i))
        
        heapify(min_heap)
        result = ListNode(0)
        ptr = result
        while min_heap:
            val, index = heappop(min_heap)
            ptr.next = ListNode(val)
            ptr = ptr.next
            
            if ptrs[index].next:
                ptrs[index] = ptrs[index].next
                heappush(min_heap, (ptrs[index].val, index))

        return result.next

from typing import List, Optional
from math import inf

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist, prev, curr, first_idx, prev_idx, curr_idx = inf, head, head.next, 0, 0, 1
        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                if prev_idx == 0:
                    first_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_idx)
                
                prev_idx = curr_idx
            
            curr_idx += 1
            prev, curr = curr, curr.next
        
        if min_dist == inf:
            return [-1, -1]

        return [min_dist, prev_idx - first_idx]

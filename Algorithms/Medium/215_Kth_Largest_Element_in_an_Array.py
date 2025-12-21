from typing import List
from heapq import heappush, heappop, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(k):
            heappush(min_heap, nums[i])
        
        for i in range(k, len(nums)):
            if min_heap[0] < nums[i]:
                heappushpop(min_heap, nums[i])
        
        return heappop(min_heap)

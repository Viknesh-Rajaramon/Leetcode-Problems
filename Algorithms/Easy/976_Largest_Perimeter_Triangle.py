from imports import *

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        max_heap = [-num for num in nums]
        heapify(max_heap)

        while len(max_heap) >= 3:
            a = -heappop(max_heap)
            b = -heappop(max_heap)
            c = -max_heap[0]

            if b + c > a:
                return a + b + c
            
            heappush(max_heap, -b)
        
        return 0

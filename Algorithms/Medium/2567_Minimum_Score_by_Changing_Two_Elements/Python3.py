from typing import List
from math import inf

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        max_heap, min_heap = [-inf] * 3, [inf] * 3
        for num in nums:
            if num < min_heap[0]:
                min_heap[0], min_heap[1], min_heap[2] = num, min_heap[0], min_heap[1]
            elif num < min_heap[1]:
                min_heap[1], min_heap[2] = num, min_heap[1]
            elif num < min_heap[2]:
                min_heap[2] = num
            
            if num > max_heap[0]:
                max_heap[0], max_heap[1], max_heap[2] = num, max_heap[0], max_heap[1]
            elif num > max_heap[1]:
                max_heap[1], max_heap[2] = num, max_heap[1]
            elif num > max_heap[2]:
                max_heap[2] = num
        
        return min(max_heap[2]-min_heap[0], max_heap[1]-min_heap[1], max_heap[0]-min_heap[2])

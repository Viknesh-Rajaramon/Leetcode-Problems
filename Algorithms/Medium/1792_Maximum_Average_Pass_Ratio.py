from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate_gain(passes: int, total_students: int) -> float:
            return passes / total_students - (passes + 1) / (total_students + 1)
        
        max_heap = []
        for passes, total in classes:
            max_heap.append((calculate_gain(passes, total), passes, total))
        
        heapify(max_heap)

        for _ in range(extraStudents):
            _, passes, total = heappop(max_heap)
            passes += 1
            total += 1
            heappush(max_heap, (calculate_gain(passes, total), passes, total))
        
        return sum(passes / total for _, passes, total in max_heap) / len(classes)

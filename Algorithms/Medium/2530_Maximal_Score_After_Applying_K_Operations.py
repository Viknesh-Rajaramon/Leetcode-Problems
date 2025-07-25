from imports import *

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapify(max_heap)
        
        score = 0
        for i in range(k):
            num = -heappop(max_heap)
            score += num
            if num == 1:
                score += k - 1 - i
                break
            heappush(max_heap, -((num + 2) // 3))

        return score

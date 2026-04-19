from typing import List
from heapq import heappop, heapify

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = [(-score[i], i) for i in range(n)]
        heapify(heap)
        result = [""] * n

        rank = 1
        while heap:
            _, i = heappop(heap)
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
            
            rank += 1
        
        return result

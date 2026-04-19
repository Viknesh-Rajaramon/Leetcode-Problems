from typing import List
from heapq import heappush, heappushpop

class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        if s.count("1") == 0:
            return 0
        
        result, max_heap = 0, []
        for i, num in enumerate(nums):
            if s[i] == "0":
                heappush(max_heap, -num)
            else:
                result += -heappushpop(max_heap, -num)

        return result

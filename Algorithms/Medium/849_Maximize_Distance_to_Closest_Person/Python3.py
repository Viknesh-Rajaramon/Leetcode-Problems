from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        
        result, prev = 0, -1
        for i in range(n):
            if seats[i] == 1:
                dist = i if prev == -1 else (i - prev) // 2
                if dist > result:
                    result = dist
                prev = i
        
        if seats[n-1] == 0:
            result = max(result, n-1-prev)
        
        return result

from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration
        for i in range(len(timeSeries)-1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)

        return total

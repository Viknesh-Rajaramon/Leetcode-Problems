from typing import List
from math import ceil, floor, sqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        V = ceil(mountainHeight / len(workerTimes))
        low, high = 1, max(workerTimes)*V*(V+1) // 2
        while low < high:
            mid = (low+high) // 2
            if sum(floor(sqrt(2*mid/t + 0.25) - 0.5) for t in workerTimes) >= mountainHeight:
                high = mid
            else:
                low = mid + 1

        return low

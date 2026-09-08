from typing import List
from heapq import heapify, heappop

class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        second_mins, min_ = [], units[0][0]
        for unit in units:
            heapify(unit)
            m = heappop(unit)
            min_ = min(min_, m)
            if unit:
                second_mins.append(heappop(unit))
            else:
                second_mins.append(m)
        
        return sum(second_mins) - min(second_mins) + min_

from typing import List
from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(min_time: int) -> bool:
            count = 0
            for r in ranks:
                count += sqrt(min_time / r) // 1
            
            return count >= cars

        l, r = 1, min(ranks) * cars * cars
        while l <= r:
            m = (l+r) // 2
            if is_possible(m):
                r = m-1
            else:
                l = m+1
        
        return l

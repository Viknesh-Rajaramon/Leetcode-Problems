from imports import *

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = (low+high) // 2

            k = 0
            for pile in piles:
                k += (pile + mid - 1) // mid
            
            if k <= h:
                high = mid
            else:
                low = mid + 1
        
        return low

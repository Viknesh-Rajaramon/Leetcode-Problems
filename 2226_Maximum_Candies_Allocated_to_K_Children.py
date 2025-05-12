from imports import *

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:        
        if sum(candies) < k:
            return 0
        
        def isPilesPossible(m: int) -> bool:
            res = 0
            for candy in candies:
                res += candy // m
            
            if res >= k:
                return True
            
            return False

        l, r = 1, sum(candies) // k
        while l < r:
            m = (l+r) // 2 + 1
            
            if isPilesPossible(m):
                l = m
            else:
                r = m-1
        
        return l

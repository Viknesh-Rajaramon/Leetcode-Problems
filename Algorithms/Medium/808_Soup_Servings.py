from math import ceil
from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0

        m = ceil(n / 25)
        
        @lru_cache(None)
        def calc_probability(A: int, B: int) -> float:
            if A <= 0 and B <= 0:
                return 0.5
            
            if A <= 0:
                return 1.0
            
            if B <= 0:
                return 0.0
            
            return 0.25 * (calc_probability(A-4, B) + calc_probability(A-3, B-1) + calc_probability(A-2, B-2) + calc_probability(A-1, B-3))

        return calc_probability(m, m)

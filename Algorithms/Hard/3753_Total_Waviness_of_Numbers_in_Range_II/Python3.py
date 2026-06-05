from typing import Optional, Tuple
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def total_waviness_upto(num: int) -> int:
            digits = list(map(int, str(num)))
            n = len(digits)
            if n < 2:
                return 0

            @lru_cache(None)
            def dfs(i: int, tight: bool, length: int, l: Optional[int], m: Optional[int]) -> Tuple[int, int]:
                if i == n:
                    return 1, 0

                limit, ways, cnt = digits[i] if tight else 9, 0, 0
                for r in range(limit+1):
                    next_tight = tight and r == limit
                    next_length, next_m = (2, m) if length > 0 else (int(r != 0), 0)
                    nways, ncnt = dfs(i+1, next_tight, next_length, next_m, r)
                    ways += nways
                    cnt += ncnt
                    if length > 1 and ((m > l and m > r) or (m < l and m < r)):
                        cnt += nways

                return ways, cnt
            
            return dfs(0, True, 0, 0, 0)[1]

        return total_waviness_upto(num2) - total_waviness_upto(num1-1)

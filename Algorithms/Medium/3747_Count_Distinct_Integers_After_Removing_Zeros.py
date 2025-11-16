from imports import *

class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        L = len(s)

        @lru_cache(None)
        def dp(i: int, tight: bool) -> int:
            if i == L:
                return 1

            total, limit = 0, int(s[i]) if tight else 9
            for d in range(1, limit+1):
                total += dp(i+1, tight and d == limit)

            return total
        
        result = 0
        for l in range(1, L):
            result += 9**l

        result += dp(0, True)
        return result

from functools import lru_cache

class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        @lru_cache(None)
        def dp(s: str, X: int) -> int:
            L = len(s)
            if L%2:
                return flatCost if X == 0 else L * X * encCost

            mid, cost = L//2, flatCost if X == 0 else L * X * encCost
            count = sum(1 for i in range(mid) if s[i] == "1")

            return min(cost, dp(s[ : mid], count) + dp(s[mid : ], X-count))
            
        return dp(s, s.count("1"))

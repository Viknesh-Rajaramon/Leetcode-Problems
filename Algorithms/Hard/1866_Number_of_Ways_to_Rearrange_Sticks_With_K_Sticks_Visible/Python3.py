from functools import lru_cache

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9+7
        
        @lru_cache(None)
        def dp(n: int, k: int) -> int:
            if n == k:
                return 1
            
            if n <= 0 or k <= 0:
                return 0
            
            return (dp(n-1, k-1) + (n-1) * dp(n-1, k)) % mod 

        return dp(n, k)

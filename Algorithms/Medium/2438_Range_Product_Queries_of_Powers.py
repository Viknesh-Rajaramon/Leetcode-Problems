from imports import *

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        
        powers, num = [], 1
        while n > 0:
            if n % 2:
                powers.append(num)
            
            n //= 2
            num *= 2
        
        m = len(powers)
        dp = [[0] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = powers[i]
            for j in range(i + 1, m):
                dp[i][j] = dp[i][j-1] * powers[j] % mod
        
        return [dp[l][r] for l, r in queries]

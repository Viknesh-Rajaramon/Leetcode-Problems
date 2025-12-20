from typing import List

MOD = 10**9 + 7

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m, n, dp = len(mat), len(mat[0]), [0] * 151
        for g in range(150, 0, -1):
            dp[g] = 1
            for i in range(m):
                dp[g] = (dp[g] * sum(1 for j in range(n) if mat[i][j] % g == 0)) % MOD
            
            for g2 in range(g*2, 151, g):
                dp[g] = (dp[g] - dp[g2] + MOD) % MOD
        
        return dp[1]

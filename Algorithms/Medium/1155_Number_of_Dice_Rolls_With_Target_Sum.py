class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        
        if n*k < target:
            return 0
        
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(i, min(i*k, target) + 1):
                for temp in range(1, min(j, k) + 1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-temp]) % mod
        
        return dp[n][target] % mod

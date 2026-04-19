class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k - 1 + maxPts <= n:
            return 1.0
        
        if k > n:
            return 0.0

        dp = [0.0] * k + [1.0] * (n + 1 - k)

        window = 1.0 * (n + 1 - k)
        for i in range(k-1, -1, -1):
            dp[i] = window / maxPts
            window += dp[i]
            
            if i+maxPts <= n:
                window -= dp[i + maxPts]
        
        return dp[0]

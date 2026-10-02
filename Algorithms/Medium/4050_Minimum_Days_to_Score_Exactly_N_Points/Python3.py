from math import inf

class Solution:
    def minDays(self, n: int) -> int:
        dp = [inf] * (n+1)
        dp[0], i = -1, 1
        while True:
            f = i*(i+1)//2
            if f > n:
                break
            
            for j in range(f, n+1):
                dp[j] = min(dp[j], dp[j-f] + i + 1)
            
            i += 1
        
        return dp[n]

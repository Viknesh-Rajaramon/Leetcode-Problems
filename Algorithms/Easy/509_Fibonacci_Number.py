dp = {0: 0, 1: 1}

class Solution:
    def fib(self, n: int) -> int:
        if n in dp:
            return dp[n]
            
        dp[n] = self.fib(n-2) + self.fib(n-1)
        return dp[n]

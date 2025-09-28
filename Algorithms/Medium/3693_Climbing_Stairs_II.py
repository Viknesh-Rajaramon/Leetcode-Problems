from imports import *

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [inf] * n
        for i in range(1, n+1):
            for step in (1, 2, 3):
                j = i - step
                if j >= 0:
                    dp[i] = min(dp[i], dp[j] + costs[i-1] + step*step)

        return dp[n]

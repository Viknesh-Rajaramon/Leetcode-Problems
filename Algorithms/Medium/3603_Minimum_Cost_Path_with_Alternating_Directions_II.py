from imports import *

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [0] * n
        dp[0] = 1

        for j in range(1, n):
            dp[j] = dp[j-1] + (j + 1) + waitCost[0][j]

        for i in range(1, m):
            dp[0] = dp[0] + waitCost[i][0] + (i + 1)
            
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + waitCost[i][j] + (i + 1) * (j + 1)
        
        return dp[n-1] - waitCost[m-1][n-1]

from imports import *

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for L in range(3, n+1):
            for i in range(n-L+1):
                j = i + L - 1
                best = inf
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    if cost < best:
                        best = cost
                
                dp[i][j] = best
        
        return dp[0][n-1]

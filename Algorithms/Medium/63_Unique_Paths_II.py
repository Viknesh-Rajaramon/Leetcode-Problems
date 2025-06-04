from imports import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = (obstacleGrid[0][0] + 1) % 2
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        
        return dp[m-1][n-1]

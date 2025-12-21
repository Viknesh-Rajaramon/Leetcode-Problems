from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [1, 1]
        for j in range(1, n):
            if grid[0][j]:
                dp[0][j] = [0, dp[0][j-1][0]]
            else:
                dp[0][j] = [dp[0][j-1][0]] * 2

        for i in range(1, m):
            if grid[i][0]:
                dp[i][0] = [dp[i-1][0][1], 0]
            else:
                dp[i][0] = [dp[i-1][0][1]] * 2

        for i in range(1, m):
            for j in range(n):
                if grid[i][j]:
                    dp[i][j] = [dp[i-1][j][1], dp[i][j-1][0]]
                else:
                    dp[i][j] = [(dp[i-1][j][1] + dp[i][j-1][0]) % mod] * 2
        
        return dp[-1][-1][0]

from typing import List

class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [1] * n
        for j in range(1, n):
            for k in range(j):
                is_valid = True
                for i in range(m):
                    if abs(grid[i][j] - grid[i][k]) > limit:
                        is_valid = False
                        break
                
                if is_valid:
                    dp[j] = max(dp[j], dp[k]+1)

        return max(dp)

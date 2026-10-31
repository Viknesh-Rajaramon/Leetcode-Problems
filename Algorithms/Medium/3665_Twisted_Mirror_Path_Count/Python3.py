from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, mod = len(grid[0]), 10**9 + 7
        dp = [0] * n
        dp[0] = 1
        for row in grid:
            prev_dp, dp, prev = dp, [0] * n, 0
            for i, val in enumerate(prev_dp):
                if row[i] == 0:
                    dp[i], prev = (prev + val) % mod, (prev + val) % mod
                else:
                    dp[i], prev = prev, val
        
        return dp[-1]

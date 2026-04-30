from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [{} for _ in range(n)]
        dp[0][k] = 0

        for i in range(m):
            for j in range(n):
                left, upper, res = dp[j-1].copy() if j > 0 else {}, dp[j].copy(), {}
                for k, v in upper.items():
                    if k not in left or left[k] < v:
                        left[k] = v

                if grid[i][j] != 0:
                    for k, v in left.items():
                        if k >= 1:
                            res[k-1] = v + grid[i][j]
                else:
                    res = left
                
                dp[j] = res
        
        return max(dp[n-1].values()) if len(dp[n-1]) != 0 else -1

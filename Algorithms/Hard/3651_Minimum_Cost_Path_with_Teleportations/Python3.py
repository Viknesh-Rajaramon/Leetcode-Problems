from typing import List
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        size = m*n

        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if i:
                    dp[i][j] = min(dp[i][j] , dp[i-1][j] + grid[i][j])
                if j:
                    dp[i][j] = min(dp[i][j] , dp[i][j-1] + grid[i][j])
        
        idx = sorted([(grid[i][j], i, j) for i in range(m) for j in range(n)], reverse = True)
        for _ in range(k):
            tp, t_min, p = [[inf] * n for _ in range(m)], inf, 0
            while p < size:
                q, v = p, idx[p][0]
                while q < size and idx[q][0] == v:
                    x, i, j = idx[q]
                    t_min = min(t_min, dp[i][j])
                    q += 1
                
                for r in range(p, q):
                    _, i, j = idx[r]
                    tp[i][j] = t_min
                
                p = q
            
            for i in range(m):
                for j in range(n):
                    if i:
                        tp[i][j] = min(tp[i][j] , tp[i-1][j] + grid[i][j])
                    if j:
                        tp[i][j] = min(tp[i][j] , tp[i][j-1] + grid[i][j])
            
            dp = tp
        
        return dp[m-1][n-1]

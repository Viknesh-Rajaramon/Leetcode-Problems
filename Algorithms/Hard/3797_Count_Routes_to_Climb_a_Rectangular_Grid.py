from typing import List
from math import sqrt

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        mod, m, n = 10**9+7, len(grid), len(grid[0])
        dp, prefix = [[0] * n for _ in range(m)], [0] * n
        for j in range(n):
            if grid[m-1][j] == ".":
                dp[m-1][j] = 1
        
        def build_prefix(i: int):
            for j in range(n):
                prefix[j] = dp[i][j] + (prefix[j-1] if j >= 1 else 0)
            
        def prefix_sum(l: int, r: int) -> int:
            return prefix[r] - (prefix[l-1] if l >= 1 else 0)
        
        for i in range(m-1, -1, -1):
            if i+1 < m:
                build_prefix(i+1)
                for j in range(n):
                    if grid[i][j] == ".":
                        offset = int(sqrt(d*d)) - 1
                        dp[i][j] = prefix_sum(max(0, j-offset), min(n-1, j+offset))
            
            build_prefix(i)
            for j in range(n):
                if grid[i][j] == ".":
                    dp[i][j] = prefix_sum(max(0, j-d), min(n-1, j+d))
        
        result = 0
        for num in dp[0]:
            result = (result + num) % mod
        
        return result

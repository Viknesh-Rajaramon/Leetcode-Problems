from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9+7
        max_prod, min_prod = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        max_prod[0][0] = min_prod[0][0] = grid[0][0]
        for i in range(1, m):
            max_prod[i][0] = min_prod[i][0] = max_prod[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            max_prod[0][j] = min_prod[0][j] = max_prod[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                vals = [max_prod[i-1][j], min_prod[i-1][j], max_prod[i][j-1], min_prod[i][j-1]]
                candidates = [grid[i][j] * num for num in vals]
                max_prod[i][j], min_prod[i][j] = max(candidates), min(candidates)

        return -1 if max_prod[m-1][n-1] < 0 else max_prod[m-1][n-1] % mod

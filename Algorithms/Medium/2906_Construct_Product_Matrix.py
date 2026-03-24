from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n, mod = len(grid), len(grid[0]), 12345
        result = [[0] * n for _ in range(m)]
        
        suffix = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                result[i][j] = suffix
                suffix = suffix * grid[i][j] % mod

        prefix = 1
        for i in range(m):
            for j in range(n):
                result[i][j] = result[i][j] * prefix % mod
                prefix = prefix * grid[i][j] % mod
        
        return result

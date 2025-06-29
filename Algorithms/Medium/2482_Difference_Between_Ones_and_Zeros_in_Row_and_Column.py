from imports import *

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(col) for col in zip(*grid)]

        m, n = len(grid), len(grid[0])
        result = [[-m-n] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] += 2 * (ones_row[i] + ones_col[j])

        return result

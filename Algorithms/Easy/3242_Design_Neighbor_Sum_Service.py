from imports import *

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.coordinates = {}
        self.n = len(grid)
        
        for i in range(self.n):
            for j in range(self.n):
                self.coordinates[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.coordinates[value]

        adj_sum = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                adj_sum += self.grid[ni][nj]
        
        return adj_sum

    def diagonalSum(self, value: int) -> int:
        i, j = self.coordinates[value]

        diag_sum = 0
        for di, dj in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                diag_sum += self.grid[ni][nj]
        
        return diag_sum


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

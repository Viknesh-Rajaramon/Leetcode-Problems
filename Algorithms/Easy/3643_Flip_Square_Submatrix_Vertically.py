from imports import *

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        z = x + k - 1
        for i in range(k // 2):
            a = x + i
            b = z - i
            for j in range(k):
                c = y + j
                grid[a][c], grid[b][c] = grid[b][c], grid[a][c]

        return grid

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m*n
        k %= total

        def shift(i: int, j: int) -> None:
            while i < j:
                grid[i//n][i%n], grid[j//n][j%n] = grid[j//n][j%n], grid[i//n][i%n]
                i += 1
                j -= 1

        shift(0, total-1)
        shift(0, k-1)
        shift(k, total-1)

        return grid

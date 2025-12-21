from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return steps

            for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                next_row, next_col = row + d_row, col + d_col
                if 0 <= next_row < n and 0 <= next_col < n and grid[next_row][next_col] == 0:
                    grid[next_row][next_col] = 1
                    queue.append((next_row, next_col, steps + 1))

        return -1

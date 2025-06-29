from imports import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque()
        fresh_oranges = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges.add((i, j))
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = 0
        while queue:
            row, col, minute = queue.popleft()
            result = max(0, minute)

            for r, c in directions:
                i, j = row + r, col + c
                if 0 <= i < m and 0 <= j < n and (i, j) in fresh_oranges:
                    queue.append((i, j, minute+1))
                    fresh_oranges.remove((i, j))
        
        return result if len(fresh_oranges) == 0 else -1

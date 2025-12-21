from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(x: int, y: int):
            queue = deque([(x, y)])
            grid[x][y] = "0"
            
            while queue:
                x, y = queue.popleft()

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"
        
        no_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                bfs(i, j)
                no_islands += 1
        
        return no_islands

from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n, directions = len(grid), len(grid[0]), [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            
            sum_ = grid[i][j]
            grid[i][j] = 0
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                    continue

                sum_ += dfs(x, y)

            return sum_
        
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                if dfs(i, j)%k == 0:
                    result += 1
        
        return result

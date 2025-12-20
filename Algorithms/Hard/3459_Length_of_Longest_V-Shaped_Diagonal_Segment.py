from typing import List
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        expected_value = [2, 2, 0]

        @lru_cache(None)
        def dfs(cx: int, cy: int, d: int, turned: bool) -> int:
            nx, ny = cx + directions[d][0], cy + directions[d][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != expected_value[grid[cx][cy]]:
                return 1
            
            max_step = dfs(nx, ny, d, turned) + 1
            if not turned:
                max_step = max(max_step, dfs(nx, ny, (d+1)%4, True) + 1)
            
            return max_step
        
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > result:
                            result = max(result, dfs(i, j, d, False))
        
        return result

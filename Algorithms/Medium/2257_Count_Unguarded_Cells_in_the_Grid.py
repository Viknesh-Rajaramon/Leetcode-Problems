from imports import *

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = 1
        
        for x, y in walls:
            grid[x][y] = 1
        
        for x, y in guards:
            up = x-1
            while up >= 0 and grid[up][y] != 1:
                grid[up][y] = 2
                up -= 1
            
            down = x+1
            while down < m and grid[down][y] != 1:
                grid[down][y] = 2
                down += 1
            
            left = y-1
            while left >= 0 and grid[x][left] != 1:
                grid[x][left] = 2
                left -= 1
            
            right = y+1
            while right < n and grid[x][right] != 1:
                grid[x][right] = 2
                right += 1
        
        return sum(row.count(0) for row in grid)

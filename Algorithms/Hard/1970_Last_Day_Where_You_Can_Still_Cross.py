from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for r, c in cells[ : day]:
                grid[r-1][c-1] = 1
            
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            queue = deque((0, j) for j in range(col) if grid[0][j] == 0)
            while queue:
                r, c = queue.popleft()
                if r == row-1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
            
            return False

        low, high = 1, len(cells)
        while low <= high:
            mid = (low+high) // 2
            if can_cross(mid):
                low = mid+1
            else:
                high = mid-1
        
        return low-1

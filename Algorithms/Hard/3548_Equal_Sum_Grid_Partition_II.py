from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def rotation(grid: List[List[int]]) -> List[List[int]]:
            m, n = len(grid), len(grid[0])
            new_grid = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    new_grid[j][m-1-i] = grid[i][j]

            return new_grid
        
        sum_ = sum(num for row in grid for num in row)
        for _ in range(4):
            m, n, exists, sum_val = len(grid), len(grid[0]), set([0]), 0
            if m < 2:
                grid = rotation(grid)
                continue
            
            if n == 1:
                for i in range(m-1):
                    sum_val += grid[i][0]
                    tag = sum_val*2 - sum_
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                
                grid = rotation(grid)
                continue
            
            for i in range(m-1):
                for j in range(n):
                    exists.add(grid[i][j])
                    sum_val += grid[i][j]
                
                tag = sum_val*2 - sum_
                if i == 0:
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                    
                    continue
                
                if tag in exists:
                    return True
            
            grid = rotation(grid)
        
        return False

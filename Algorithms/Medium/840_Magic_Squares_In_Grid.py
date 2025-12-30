from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r: int, c: int):
            if grid[r][c] != 5:
                return False

            s, row_sum, col_sum = [False] * 10, [0] * 3, [0] * 3
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if grid[i][j] < 1 or grid[i][j] > 9 or s[grid[i][j]]:
                        return False
                    
                    row_sum[i-r+1] += grid[i][j]
                    col_sum[j-c+1] += grid[i][j]
                    s[grid[i][j]] = True
            
            if not all(s[1:]) or any(rs != 15 for rs in row_sum) or any(cs != 15 for cs in col_sum):
                return False
            
            return grid[r-1][c-1]+grid[r+1][c+1] == 10 and grid[r-1][c+1]+grid[r+1][c-1] == 10
        
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        
        return sum(1 for r in range(1, m-1) for c in range(1, n-1) if is_magic(r, c))

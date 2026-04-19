from typing import List
from math import inf

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        min_row, max_row, min_col, max_col, row_not_set = 0, 0, inf, 0, True
        for i in range(len(grid)):
            if 1 not in grid[i]:
                continue
            
            if row_not_set:
                min_row = i
                row_not_set = False
                
            max_row = i

            rev_row = grid[i][::-1]
            min_col = min(min_col, grid[i].index(1))
            max_col = max(max_col, n - rev_row.index(1))

        return (max_row - min_row + 1) * (max_col - min_col)

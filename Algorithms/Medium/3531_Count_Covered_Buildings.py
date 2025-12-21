from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_row_indices, max_row_indices = [n+1] * (n+1), [0] * (n+1)
        min_col_indices, max_col_indices = [n+1] * (n+1), [0] * (n+1)

        for row, col in buildings:
            if row < min_row_indices[col]:
                min_row_indices[col] = row
            
            if row > max_row_indices[col]:
                max_row_indices[col] = row
            
            if col < min_col_indices[row]:
                min_col_indices[row] = col
            
            if col > max_col_indices[row]:
                max_col_indices[row] = col
            
        result = 0
        for row, col in buildings:
            if min_row_indices[col] < row < max_row_indices[col] and min_col_indices[row] < col < max_col_indices[row]:
                result += 1
        
        return result

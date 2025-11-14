from imports import *

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            result[row1][col1] += 1
            end_row, end_col = row2+1, col2+1
            if end_row < n:
                result[end_row][col1] -= 1
            
            if end_col < n:
                result[row1][end_col] -= 1
            
            if end_row < n and end_col < n:
                result[end_row][end_col] += 1
        
        for row in range(n):
            for col in range(n):
                if row > 0:
                    result[row][col] += result[row-1][col]
                
                if col > 0:
                    result[row][col] += result[row][col-1]
                
                if row > 0 and col > 0:
                    result[row][col] -= result[row-1][col-1]
            
        return result

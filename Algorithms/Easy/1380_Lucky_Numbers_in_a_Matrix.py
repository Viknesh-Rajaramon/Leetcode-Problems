from imports import *

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min, col_max = defaultdict(int), defaultdict(int)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][row_min[i]] > matrix[i][j]:
                    row_min[i] = j
                
                if matrix[col_max[j]][j] < matrix[i][j]:
                    col_max[j] = i

        return [matrix[r][c] for r, c in row_min.items() if col_max[c] == r]

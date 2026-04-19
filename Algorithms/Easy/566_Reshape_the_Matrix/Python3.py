from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m == r and n == c:
            return mat
        
        if m *n != r*c:
            return mat

        new_matrix = [[0] * c for _ in range(r)]
        for i in range(m*n):
            new_matrix[i//c][i%c] = mat[i//n][i%n]

        return new_matrix

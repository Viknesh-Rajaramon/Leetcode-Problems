from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        result = 0
        for i in range(m):
            if row[i] != 1:
                continue
            
            for j in range(n):
                if col[j] != 1:
                    continue
                
                if mat[i][j] == 1:
                    result += 1

        return result

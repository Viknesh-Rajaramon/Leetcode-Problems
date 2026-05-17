from typing import List
from collections import defaultdict

class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        m, n, pos = len(matrix), len(matrix[0]), defaultdict(list)
        for i in range(m):
            for j in range(n):
                pos[matrix[i][j]].append((i, j))
        
        result = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    continue
                
                ok = True
                for val in range(matrix[r][c]+1, 201):
                    for nr, nc in pos[val]:
                        dr, dc = abs(nr-r), abs(nc-c)
                        if dr <= matrix[r][c] and dc <= matrix[r][c]:
                            if dr == matrix[r][c] and dc == matrix[r][c]:
                                continue
                            
                            ok = False
                            break

                    if not ok:
                        break
                    
                if ok:
                    result += 1

        return result

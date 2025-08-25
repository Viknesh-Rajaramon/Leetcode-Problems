from imports import *

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []

        m, n = len(mat), len(mat[0])
        i, j, reverse = 0, 0, False
        for _ in range(m*n):
            result.append(mat[i][j])
            
            if not reverse:
                if j == n-1:
                    i += 1
                    reverse = True
                elif i == 0:
                    j += 1
                    reverse = True
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                    reverse = False
                elif j == 0:
                    i += 1
                    reverse = False
                else:
                    i += 1
                    j -= 1
        
        return result

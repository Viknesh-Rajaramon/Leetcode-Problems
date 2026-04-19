from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                P[i+1][j+1] = P[i][j+1] + row_sum
    
        def does_square_exist(k: int) -> bool:
            for i in range(k, m+1):
                for j in range(k, n+1):
                    if P[i][j] - P[i-k][j] - P[i][j-k] + P[i-k][j-k] <= threshold:
                        return True

            return False
        
        result = 0
        for k in range(1, min(m, n)+1):
            if does_square_exist(k):
                result += 1
            else:
                break

        return result

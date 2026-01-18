from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sum = [[0] * n for _ in range(m)]
        for i in range(m):
            row_sum[i][0] = grid[i][0]
            for j in range(1, n):
                row_sum[i][j] = row_sum[i][j-1] + grid[i][j]
        
        col_sum = [[0] * n for _ in range(m)]
        for j in range(n):
            col_sum[0][j] = grid[0][j]
            for i in range(1, m):
                col_sum[i][j] = col_sum[i-1][j] + grid[i][j]
        
        for size in range(min(m, n), 1, -1):
            for i in range(m-size+1):
                for j in range(n-size+1):
                    sum_, check = row_sum[i][j+size-1] - (0 if j == 0 else row_sum[i][j-1]), True
                    for ii in range(i+1, i+size):
                        if row_sum[ii][j+size-1] - (0 if j == 0 else row_sum[ii][j-1]) != sum_:
                            check = False
                            break

                    if not check:
                        continue
                    
                    for jj in range(j, j+size):
                        if col_sum[i+size-1][jj] - (0 if i == 0 else col_sum[i-1][jj]) != sum_:
                            check = False
                            break

                    if not check:
                        continue

                    d1, d2 = 0, 0
                    for k in range(size):
                        d1 += grid[i+k][j+k]
                        d2 += grid[i+k][j+size-1-k]

                    if d1 == sum_ and d2 == sum_:
                        return size

        return 1

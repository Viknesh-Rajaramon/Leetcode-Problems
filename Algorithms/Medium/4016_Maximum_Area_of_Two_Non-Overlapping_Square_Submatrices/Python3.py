from typing import List

class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp, row_max, col_max = [[0] * n for _ in range(m)], [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                
                row_max[i] = max(row_max[i], dp[i][j])
                col_max[j] = max(col_max[j], dp[i][j])
        
        row_suffix = [0] * (m + 1)
        for i in range(m-1, -1, -1):
            row_suffix[i] = max(row_suffix[i+1], row_max[i])

        col_suffix = [0] * (n + 1)
        for j in range(n-1, -1, -1):
            col_suffix[j] = max(col_suffix[j+1], col_max[j])

        result = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] <= result:
                    continue

                if i+dp[i][j] < m and row_suffix[i+dp[i][j]] >= dp[i][j]:
                    result = dp[i][j]
                    continue

                if j+dp[i][j] < n and col_suffix[j+dp[i][j]] >= dp[i][j]:
                    result = dp[i][j]

        return result**2

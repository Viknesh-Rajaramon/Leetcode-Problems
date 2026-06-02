from math import inf

class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        result, m, n = -inf, len(grid), len(grid[0])
        for i in range(1, m-1):
            for j in range(1, n-1):
                result = max(result, grid[i][j])
        
        for i in range(m):
            curr_sum = grid[i][0]
            for j in range(1, n):
                curr_sum = max(curr_sum, grid[i][j-1]) + grid[i][j]
                result = max(result, curr_sum)

        for j in range(n):
            curr_sum = grid[0][j]
            for i in range(1, m):
                curr_sum = max(curr_sum, grid[i-1][j]) + grid[i][j]
                result = max(result, curr_sum)
        
        return result

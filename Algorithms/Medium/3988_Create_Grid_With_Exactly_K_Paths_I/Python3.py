class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        grid, dp, r, c = [['#'] * n for _ in range(m)], [[0] * n for _ in range(m)], min(m, 4), min(n, 4)
        def backtrack(i: int, j: int) -> bool:
            if i == r:
                return dp[r-1][c-1] == k
            
            next_i, next_j = i, j+1
            if next_j == c:
                next_i, next_j = i+1, 0
            
            grid[i][j] = '.'
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)
            
            if backtrack(next_i, next_j):
                return True
            
            grid[i][j], dp[i][j] = '#', 0
            if not ((i == 0 and j == 0) or (i == r-1 and j == c-1)):
                if backtrack(next_i, next_j):
                    return True
            
            return False
        
        if not backtrack(0, 0):
            return []

        for j in range(c-1, n):
            grid[r-1][j] = '.'
        
        for i in range(r-1, m):
            grid[i][n-1] = '.'
        
        return ["".join(row) for row in grid]

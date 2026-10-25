class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        result, m, n = 0, len(grid), len(grid[0])
        def dfs(r: int, c: int) -> bool:
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            if grid[r][c] == 1:
                return True
            
            grid[r][c] = 1
            left, right, up, down = dfs(r, c-1), dfs(r, c+1), dfs(r-1, c), dfs(r+1, c)
            return left and right and up and down

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and dfs(r, c):
                    result += 1

        return result

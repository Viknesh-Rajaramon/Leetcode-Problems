class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n, r, c = len(grid), len(grid[0]), 0, 0
        while True:
            move = grid[r][c]
            grid[r][c], nr, nc = 'V', r, c
            if move == 'R':
                nc += 1
            elif move == 'L':
                nc -= 1
            elif move == 'D':
                nr += 1
            elif move == 'U':
                nr -= 1

            if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 'V':
                return [r, c]

            r, c = nr, nc
        
        return [r, c]

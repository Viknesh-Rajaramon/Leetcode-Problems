from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {
            1: {0, 1},
            2: {2, 3},
            3: {0, 3},
            4: {1, 3},
            5: {0, 2},
            6: {1, 2},
        }
        moves = [(0, -1, 0, 1), (0, 1, 1, 0), (-1, 0, 2, 3), (1, 0, 3, 2)]
        queue, visited = deque([(0, 0)]), set([(0, 0)])
        while queue:
            row, col = queue.popleft()
            if row == m-1 and col == n-1:
                return True
            
            for dr, dc, dx, dy in moves:
                nr, nc = row+dr, col+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited:
                    continue

                if dx not in dirs[grid[row][col]] or dy not in dirs[grid[nr][nc]]:
                    continue

                visited.add((nr, nc))
                queue.append((nr, nc))

        return False

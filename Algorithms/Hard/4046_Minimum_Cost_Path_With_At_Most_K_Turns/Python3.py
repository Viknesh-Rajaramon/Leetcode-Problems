from math import inf
from heapq import heappop, heappush

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        
        dirs, queue = [(0, 1), (1, 0), (0, -1), (-1, 0)], [(grid[0][0], 0, 0, -1, 0)]
        k += 1
        dist, dp = [[inf] * n for _ in range(m)], [[[inf] * 4 for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0
        while queue:
            val, r, c, prev_dir, moves = heappop(queue)
            if r == m-1 and c == n-1 and moves <= k:
                return val

            if prev_dir != -1:
                if moves >= dp[r][c][prev_dir]:
                    continue
                
                dp[r][c][prev_dir] = moves

            for d in range(4):
                nr, nc, new_moves = r + dirs[d][0], c + dirs[d][1], moves + (1 if d != prev_dir else 0)
                if nr < 0 or nc < 0 or nr >= m or nc >= n or dist[nr][nc] < new_moves or new_moves > k:
                    continue 
                
                dist[nr][nc] = new_moves
                heappush(queue, (val + grid[nr][nc], nr, nc, d, new_moves))
        
        return -1

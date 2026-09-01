from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        dp = [[-1] * n for _ in range(m)]
        k, sr, sc = 0, 0, 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    sr, sc = r, c
                elif classroom[r][c] == "L":
                    dp[r][c] = k
                    k += 1
        
        if k == 0:
            return 0
        
        total_mask, best = (1 << k) - 1, [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        best[sr][sc][0], directions = energy, [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(sr, sc, 0, energy, 0)])
        while queue:
            r, c, mask, e, moves = queue.popleft()
            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or classroom[nr][nc] == "X":
                    continue
                
                ne, nmask = e-1, mask
                if classroom[nr][nc] == "R":
                    ne = energy
                
                if classroom[nr][nc] == "L":
                    nmask |= 1 << dp[nr][nc]
                
                if nmask == total_mask:
                    return moves+1
                
                if ne <= best[nr][nc][nmask]:
                    continue
                
                best[nr][nc][nmask] = ne
                queue.append((nr, nc, nmask, ne, moves+1))
        
        return -1

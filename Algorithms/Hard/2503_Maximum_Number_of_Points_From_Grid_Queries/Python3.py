from typing import List
from heapq import heappop, heappush

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n, k = len(grid), len(grid[0]), len(queries)
        result, directions = [0] * k, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap, grid[0][0], points = [(grid[0][0], 0, 0)], 0, 0
        for val, idx in sorted([(queries[i], i) for i in range(k)]):
            while len(heap) > 0 and heap[0][0] < val:
                _, i, j = heappop(heap)
                points += 1

                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if (0 <= nr < m and 0 <= nc < n and grid[nr][nc]):
                        heappush(heap, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0

            result[idx] = points

        return result

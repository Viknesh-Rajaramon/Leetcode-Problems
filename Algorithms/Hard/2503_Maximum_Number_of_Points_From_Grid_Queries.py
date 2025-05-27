from imports import *

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)
        
        ans = [0] * k
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        heap = [(grid[0][0], 0, 0)]
        heapify(heap)
        grid[0][0] = 0
        points = 0
        
        for val, idx in sorted([(queries[i], i) for i in range(k)]):
            while len(heap) > 0 and heap[0][0] < val:
                _, i, j = heappop(heap)
                points += 1

                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if (0 <= nr < m and 0 <= nc < n and grid[nr][nc]):
                        heappush(heap, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0

            ans[idx] = points

        return ans

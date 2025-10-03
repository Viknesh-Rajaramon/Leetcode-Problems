from imports import *

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        visited, boundary = set(), []
        for i in range(m):
            heappush(boundary, (heightMap[i][0], i, 0))
            visited.add((i, 0))
            heappush(boundary, (heightMap[i][n-1], i, n-1))
            visited.add((i, n-1))
        
        for i in range(n):
            heappush(boundary, (heightMap[0][i], 0, i))
            visited.add((0, i))
            heappush(boundary, (heightMap[m-1][i], m-1, i))
            visited.add((m-1, i))
        
        result = 0
        while boundary:
            curr_height, row, col = heappop(boundary)

            for d_r, d_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                r, c = row + d_r, col + d_c

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    if heightMap[r][c] < curr_height:
                        result += curr_height - heightMap[r][c]
                
                    heappush(boundary, (max(heightMap[r][c], curr_height), r, c))
                    visited.add((r, c))

        return result

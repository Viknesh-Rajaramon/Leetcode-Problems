from imports import *

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def dfs(visited: set, r: int, c: int):
            if (r, c) in visited:
                return

            visited.add((r, c))
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = r + di, c + dj
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[r][c] <= heights[x][y]:
                    dfs(visited, x, y)

        pacific_visited, atlantic_visited = set(), set()
        for i in range(m):
            dfs(pacific_visited, i, 0)
            dfs(atlantic_visited, i, n-1)

        for j in range(n):
            dfs(pacific_visited, 0, j)
            dfs(atlantic_visited, m-1, j)
        
        return list(map(list, pacific_visited & atlantic_visited))

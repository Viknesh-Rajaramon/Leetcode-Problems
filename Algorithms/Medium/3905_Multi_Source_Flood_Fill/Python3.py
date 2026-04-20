from collections import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key = lambda x: -x[2])
        result, queue = [[-1] * m for _ in range(n)], deque()
        for r, c, color in sources:
            result[r][c] = color
            queue.append((r, c, color))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j, color = queue.popleft()
            for dx, dy in directions:
                nx, ny = i+dx, j+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or result[nx][ny] != -1:
                    continue

                result[nx][ny] = color
                queue.append((nx, ny, color))

        return result

from imports import *

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])

        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if "A" <= matrix[i][j] <= "Z":
                    portals[matrix[i][j]].append((i, j))

        queue = deque([(0, 0, 0)])
        visited = set()
        used_portals = set()

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (m - 1, n - 1):
                return steps
            
            cell = matrix[row][col]
            if "A" <= cell <= "Z" and cell not in used_portals:
                used_portals.add(cell)

                for portal_row, portal_col in portals[cell]:
                    if (portal_row, portal_col) not in visited:
                        visited.add((portal_row, portal_col))
                        queue.append((portal_row, portal_col, steps))
            else:
                visited.add((row, col))

            for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited and matrix[new_row][new_col] != "#":
                    cell = matrix[new_row][new_col]
                    if "A" <= cell <= "Z" and cell not in used_portals:
                        used_portals.add(cell)

                        for portal_row, portal_col in portals[cell]:
                            if (portal_row, portal_col) not in visited:
                                visited.add((portal_row, portal_col))
                                queue.append((portal_row, portal_col, steps + 1))
                    else:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, steps + 1))
                    
        return -1

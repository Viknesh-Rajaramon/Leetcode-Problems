class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        result, m, n = 0, len(grid), len(grid[0])
        for r in range(m):
            count, idx = 0, -1
            for c in range(n):
                if grid[r][c] == 1:
                    if count == 0:
                        idx = c
                    
                    count += 1

            can_comm = (count != 1)
            if not can_comm:
                for i in range(m):
                    if i != r and grid[i][idx] == 1:
                        can_comm = True
                        break

            if can_comm:
                result += count

        return result

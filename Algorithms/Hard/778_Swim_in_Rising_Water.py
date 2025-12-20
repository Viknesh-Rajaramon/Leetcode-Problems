from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(u: int, v: int, t: int, visited: set) -> bool:
            if u == n-1 and v == n-1:
                return True
            
            visited.add((u, v))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = u + di, v + dj
                if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] <= t:
                    if dfs(r, c, t, visited):
                        return True
            
            return False
        
        low, high = max(grid[0][0], grid[n-1][n-1]), n*n - 1
        result = high
        while low <= high:
            mid = (low + high) // 2
            if dfs(0, 0, mid, set()):
                high = mid - 1
                result = mid
            else:
                low = mid + 1
        
        return result

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        class UF:
            def __init__(self, n: int):
                self.n = n
                self.parent = list(range(n))
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> bool:
                x, y = self.find(x), self.find(y)
                if x != y:
                    self.parent[y] = x
                    return True
                
                return False
            
        m, n = len(grid), len(grid[0])
        uf = UF(m*n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    if not uf.union(i*n+j, (i-1)*n+j):
                        return True
                
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    if not uf.union(i*n+j, i*n+j-1):
                        return True
        
        return False

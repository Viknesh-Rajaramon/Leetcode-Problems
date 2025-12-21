from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        class UF:
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.components = n
            
            def find(self, x) -> int:
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> None:
                x, y = self.find(x), self.find(y)
                
                if x != y:
                    self.parent[y] = x
                    self.components -= 1
        
        uf = UF(n)
        edges.sort(key = lambda x: x[2])

        for u, v, w in edges:
            uf.union(u, v)
            if uf.components == k:
                return w
        
        return 0

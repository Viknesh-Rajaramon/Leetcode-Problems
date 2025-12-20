from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class UF:
            def __init__(self, n: int):
                self.parent = list(range(n))
            
            def find(self, x: int) -> int:
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> bool:
                x, y = self.find(x), self.find(y)
                if x == y:
                    return False

                self.parent[x] = y
                return True
        
        uf = UF(n)
        must_edges, opt_edges = [], []
        tree_edges = 0

        for u, v, s, m in edges:
            if m == 0:
                opt_edges.append((u, v, s))
            else:
                if not uf.union(u, v):
                    return -1

                must_edges.append((u, v, s))
                tree_edges += 1
        
        if tree_edges > n-1:
            return -1
        
        opt_edges.sort(key = lambda x: -x[2])
        selected = []

        for u, v, s in opt_edges:
            if tree_edges == n-1:
                break
            
            if uf.union(u, v):
                selected.append((u, v, s))
                tree_edges += 1
        
        if tree_edges != n-1:
            return -1

        strengths = [s for _, _, s in selected]
        strengths.sort()
        for i in range(min(k, len(strengths))):
            strengths[i] *= 2

        return min([s for _, _, s in must_edges] + strengths)

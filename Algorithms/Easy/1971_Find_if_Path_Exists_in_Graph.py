from imports import *

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        roots = list(range(n))
        def find(node: int) -> int:
            if node == roots[node]:
                return node
            
            roots[node] = find(roots[node])
            return roots[node]
        
        for u, v in edges:
            roots[find(u)] = find(v)

        return find(source) == find(destination)

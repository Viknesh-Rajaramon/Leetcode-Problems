from collections import defaultdict
from math import inf

class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        graph = defaultdict(list)
        for u, v, c in edges:
            graph[u].append((v, c))
            graph[v].append((u, c))
        
        result = inf
        def dfs(u: int, parent: int) -> list[int, int]:
            nonlocal result
            b, f = values[u].bit_count() & 1, [inf, inf]
            f[b] = 0
            for v, c in graph[u]:
                if v == parent:
                    continue
                
                g = dfs(v, u)
                result = min(result, min(f[0]+g[0], f[1]+g[1])+c)
                f[b] = min(f[b], g[0] + c)
                f[b^1] = min(f[b^1], g[1] + c)

            return f

        dfs(0, -1)
        return result if result != inf else -1

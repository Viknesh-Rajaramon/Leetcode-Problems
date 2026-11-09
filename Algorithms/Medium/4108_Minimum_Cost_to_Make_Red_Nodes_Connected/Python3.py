from typing import List

class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u: int, parent: int) -> List[int]:
            size, cost_B, cost_R, t = 1, 0, 0, []
            for v in g[u]:
                if v == parent:
                    continue
                
                sz, c_B, c_R, c_BR = dfs(v, u)
                size += sz
                cost_B += c_B
                cost_R += min(c_R, c_B)
                t.append(c_B - min(c_R, c_BR))
            
            t.sort(reverse = True)
            cost_B += 0 if colors[u] == 'B' else size
            cost_R += 0 if colors[u] == 'R' else size

            cost_BR = cost_B - t[0] if t else 0
            return size, cost_B, cost_R, cost_BR
        
        return min(dfs(0, -1)[1 : ])

from imports import *

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(v, res):
            if v in visited:
                return
            
            visited.add(v)
            res.append(v)
            for neighbor in adj_list[v]:
                dfs(neighbor, res)
            
            return res
        
        ans = 0
        for v in range(n):
            if v in visited:
                continue
            
            component = dfs(v, [])
            if all([len(component)-1 == len(adj_list[v2]) for v2 in component]):
                ans += 1
        
        return ans

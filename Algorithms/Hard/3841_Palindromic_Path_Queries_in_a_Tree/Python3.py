from collections import defaultdict

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        LOG, timer = 17, 0
        parent, depth, tin, tout = [[-1] * n for _ in range(LOG)], [0] * n, [0] * n, [0] * n
        def dfs(node: int, par: int) -> None:
            nonlocal timer
            tin[node], parent[0][node] = timer, par
            timer += 1
            
            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                
                depth[neighbor] = depth[node] + 1
                dfs(neighbor, node)
        
            tout[node] = timer - 1
        
        dfs(0, -1)

        for i in range(1, LOG):
            for j in range(n):
                p = parent[i-1][j]
                if p != -1:
                    parent[i][j] = parent[i-1][p]
        
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if diff & (1 << i):
                    u = parent[i][u]
            
            if u == v:
                return u
            
            for i in range(LOG-1, -1, -1):
                if parent[i][u] != parent[i][v]:
                    u, v = parent[i][u], parent[i][v]
            
            return parent[0][u]
        
        fenwick = [0] * (n+1)
        def fenwick_add(i: int, val: int) -> None:
            i += 1
            while i <= n:
                fenwick[i] ^= val
                i += i & -i
            
        def fenwick_prefix(i: int) -> int:
            result = 0
            i += 1
            while i > 0:
                result ^= fenwick[i]
                i -= i & -i
            
            return result
        
        def char_mask(c: str) -> int:
            return 1 << (ord(c) - 97)
        
        labels = list(s)
        for u, c in enumerate(labels):
            m = char_mask(c)
            fenwick_add(tin[u], m)
            fenwick_add(tout[u]+1, m)
        
        result = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                delta = char_mask(labels[u]) ^ char_mask(c)
                labels[u] = c
                fenwick_add(tin[u], delta)
                fenwick_add(tout[u]+1, delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                path_mask = fenwick_prefix(tin[u]) ^ fenwick_prefix(tin[v]) ^ char_mask(labels[w])
                result.append(path_mask == 0 or (path_mask & (path_mask-1)) == 0)

        return result

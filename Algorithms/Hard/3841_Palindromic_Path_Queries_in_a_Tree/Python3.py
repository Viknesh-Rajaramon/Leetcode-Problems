from collections import defaultdict

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n+1)

    def update(self, i: int, val: int) -> None:
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def query(self, i: int) -> int:
        result = 0
        while i > 0:
            result ^= self.tree[i]
            i -= i & -i
        
        return result
    
    def update_range(self, l: int, r: int, val: int) -> None:
        self.update(l, val)
        self.update(r+1, val)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        LOG, timer = n.bit_length(), 0
        parent, depth, tin, tout = [[0] * LOG for _ in range(n)], [0] * n, [0] * n, [0] * n
        def dfs(u: int, par: int) -> None:
            nonlocal timer
            timer += 1
            tin[u], parent[u][0] = timer, par
            for v in graph[u]:
                if v == par:
                    continue
                
                depth[v] = depth[u]+1
                dfs(v, u)
        
            tout[u] = timer
        
        dfs(0, 0)
        for j in range(1, LOG):
            for i in range(n):
                parent[i][j] = parent[parent[i][j-1]][j-1]
        
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if diff & (1 << i):
                    u = parent[u][i]
            
            if u == v:
                return u
            
            for i in range(LOG-1, -1, -1):
                if parent[u][i] != parent[v][i]:
                    u, v = parent[u][i], parent[v][i]
            
            return parent[u][0]
        
        ft, labels = FenwickTree(n+1), list(s)
        for u, c in enumerate(labels):
            ft.update_range(tin[u], tout[u], 1 << (ord(c) - 97))
        
        result = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                ft.update_range(tin[u], tout[u], (1 << (ord(labels[u]) - 97)) ^ (1 << (ord(c) - 97)))
                labels[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                path_mask = ft.query(tin[u]) ^ ft.query(tin[v]) ^ (1 << (ord(labels[lca(u, v)]) - 97))
                result.append((path_mask & (path_mask-1)) == 0)

        return result

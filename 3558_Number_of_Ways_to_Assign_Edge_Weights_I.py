from imports import *

MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        max_depth = 0
        visited = set()
        def dfs(u: int, depth: int) -> int:
            visited.add(u)
            for v in tree[u]:
                if v not in visited:
                    dfs(v, depth + 1)

            nonlocal max_depth
            max_depth = max(max_depth, depth)

        dfs(1, 0)
        return pow(2, max_depth - 1, MOD)

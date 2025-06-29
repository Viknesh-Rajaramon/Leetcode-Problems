from imports import *

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        result = 0
        def dfs(child: int, parent: int) -> int:
            if len(tree[child]) == 1 and tree[child][0] == parent:
                return cost[child]
            
            path_cost = []
            for node in tree[child]:
                if node != parent:
                    path_cost.append(dfs(node, child))
            
            max_cost = max(path_cost)
            for c in path_cost:
                if c != max_cost:
                    nonlocal result
                    result += 1
            
            return max_cost + cost[child]

        dfs(0, -1)
        return result

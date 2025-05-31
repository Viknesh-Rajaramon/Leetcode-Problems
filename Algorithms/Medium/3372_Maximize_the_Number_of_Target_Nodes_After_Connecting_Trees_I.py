from imports import *

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_tree(edges: List[List[int]]) -> dict:
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            
            return tree
        
        def dfs(tree: dict, visited: set, u: int, limit: int) -> int:
            if limit == 0:
                return 0
            
            visited.add(u)
            count = 1
            for v in tree[u]:
                if v not in visited:
                    visited.add(v)
                    count += dfs(tree, visited, v, limit-1)

            return count

        tree1 = build_tree(edges1)
        tree2 = build_tree(edges2)

        max_dist = max(dfs(tree2, set(), i, k) for i in range(len(edges2)+1))
        return [dfs(tree1, set(), i, k+1) + max_dist for i in range(len(edges1)+1)] 

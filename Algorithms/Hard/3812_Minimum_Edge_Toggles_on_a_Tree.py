from typing import List
from collections import defaultdict

class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        tree, ind, diff = defaultdict(list), 0, [int(start[i]) ^ int(target[i]) for i in range(n)]
        for u, v in edges:
            tree[u].append((v, ind))
            tree[v].append((u, ind))
            ind += 1
        
        result = []
        def dfs(u: int, parent: int, ind: int) -> bool:
            c_diff = diff[u]
            for v, idx in tree[u]:
                if v == parent:
                    continue
                
                if dfs(v, u, idx):
                    c_diff ^= 1
                
            if c_diff:
                if parent == -1:
                    return True
                
                result.append(ind)
                return True
            
            return False

        cannot_transform = dfs(0, -1, -1)
        return sorted(result) if not cannot_transform else [-1]

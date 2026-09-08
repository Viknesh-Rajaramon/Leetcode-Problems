from typing import List
from math import inf

class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
        
        def dfs(u: int):
            if not tree[u]:
                return baseTime[u]
            
            earliest, latest = inf, -inf
            for v in tree[u]:
                finish = dfs(v)
                earliest, latest = min(earliest, finish), max(latest, finish)
            
            return latest + (latest - earliest) + baseTime[u]
        
        return dfs(0)

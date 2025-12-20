from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        result, graph = 0, defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int) -> int:
            curr_sum = values[node]
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                curr_sum += dfs(neighbor, node)
            
            curr_sum %= k
            if curr_sum == 0:
                nonlocal result
                result += 1
                return 0
            
            return curr_sum
        
        dfs(0, -1)
        return result

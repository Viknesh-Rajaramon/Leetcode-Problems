from imports import *

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node: int, path: List[int]) -> None:
            if node == len(graph)-1:
                result.append(path)
                return
            
            for v in graph[node]:
                dfs(v, path + [v])
        
        dfs(0, [0])
        return result

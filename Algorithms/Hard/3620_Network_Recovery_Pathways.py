from imports import *

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
        
        to_visit = [(-inf, 0, 0)]
        visited = [-1] * n

        while to_visit:
            min_edge, curr_cost, node = heappop(to_visit)
            min_edge = -min_edge

            if visited[node] != -1 and visited[node] <= curr_cost:
                continue
            
            visited[node] = curr_cost

            if node == n-1:
                return min_edge
            
            for neighbor, cost in graph[node]:
                new_cost = cost + curr_cost
                if new_cost <= k:
                    heappush(to_visit, (-min(min_edge, cost), new_cost, neighbor))
        
        return -1

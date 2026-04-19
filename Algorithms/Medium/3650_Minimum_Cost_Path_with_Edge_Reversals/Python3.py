from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2*w))
        
        dist, min_heap = [inf] * n, [(0, 0)]
        dist[0] = 0
        while min_heap:
            cost, u = heappop(min_heap)
            if u == n-1:
                return cost
            
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heappush(min_heap, (new_cost, v))
        
        return -1

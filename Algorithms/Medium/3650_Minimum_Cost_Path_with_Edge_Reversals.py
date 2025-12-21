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
        
        dist = defaultdict(lambda: inf)
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            cost, u = heappop(heap)
            if u == n-1:
                return cost
            
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heappush(heap, (new_cost, v))
        
        return -1

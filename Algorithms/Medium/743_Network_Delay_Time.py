from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(dict)
        for u, v, w in times:
            edges[u][v] = w
        
        dist = {node: inf for node in range(1, n + 1)}
        dist[k] = 0

        heap = [(0, k)]
        while heap:
            w, u = heappop(heap)
            if w > dist[u]:
                continue
            
            for v, t in edges[u].items():
                new_w = t + w
                if new_w < dist[v]:
                    dist[v] = new_w
                    heappush(heap, (new_w, v))
        
        max_ = max(dist.values())
        return max_ if max_ < inf else -1

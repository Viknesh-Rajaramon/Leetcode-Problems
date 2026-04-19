from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        
        dist = [inf] * n
        dist[0] = 0

        heap = [(0, 0)]
        while heap:
            t, u = heappop(heap)
            if u == n-1:
                return t

            if t > dist[u]:
                continue
            
            for v, start, end in graph[u]:
                if t > end:
                    continue
                
                new_t = max(t, start) + 1
                if new_t >= dist[v]:
                    continue
                
                dist[v] = new_t
                heappush(heap, (new_t, v))
        
        return -1

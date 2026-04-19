from typing import List
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for src, dest, w in zip(original, changed, cost):
            graph[ord(src)-ord("a")].append((ord(dest)-ord("a"), w))
        
        def dijkstra(start: int) -> List[int]:
            dist, min_heap = [inf] * 26, [(0, start)]
            dist[start] = 0
            while min_heap:
                d, u = heappop(min_heap)
                if d > dist[u]:
                    continue
                
                for v, w in graph[u]:
                    new_d = d + w
                    if new_d < dist[v]:
                        dist[v] = new_d
                        heappush(min_heap, (new_d, v))
            
            return dist

        result, min_cost = 0, [dijkstra(i) for i in range(26)]
        for s, t in zip(source, target):
            src, dest = ord(s) - ord("a"), ord(t) - ord("a")
            if min_cost[src][dest] == inf:
                return -1
            
            result += min_cost[src][dest]

        return result

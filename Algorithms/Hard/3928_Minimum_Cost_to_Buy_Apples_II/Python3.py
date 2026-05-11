from typing import List
from collections import defaultdict
from math import inf
from heapq import heappush, heappop

class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        empty_graph, carry_graph = defaultdict(list), defaultdict(list)
        for u, v, cost, tax in roads:
            empty_graph[u].append((v, cost))
            empty_graph[v].append((u, cost))

            carry_graph[u].append((v, cost*tax))
            carry_graph[v].append((u, cost*tax))
        
        def dijkstras(src: int, graph: defaultdict) -> list[int]:
            dist, min_heap = [inf] * n, [(0, src)]
            dist[src] = 0
            while min_heap:
                d, u = heappop(min_heap)
                if d > dist[u]:
                    continue
                
                for v, w in graph[u]:
                    if dist[v] > d+w:
                        dist[v] = d+w
                        heappush(min_heap, (dist[v], v))
            
            return dist
        
        result = [0] * n
        for src in range(n):
            empty_dist, carry_dist = dijkstras(src, empty_graph), dijkstras(src, carry_graph)
            best = prices[src]
            for shop in range(n):
                if empty_dist[shop] == inf or carry_dist[shop] == inf:
                    continue
                
                best = min(best, empty_dist[shop] + carry_dist[shop] + prices[shop])
            
            result[src] = best

        return result

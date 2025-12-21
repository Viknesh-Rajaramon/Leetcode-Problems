from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v, t in roads:
            adj_list[u].append((t, v))
            adj_list[v].append((t, u))

        mod = 10**9 + 7
        min_heap = [(0, 0)]
        min_cost = [inf] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)
            if cost > min_cost[n-1]:
                continue

            for w, nei in adj_list[node]:
                if cost + w < min_cost[nei]:
                    min_cost[nei] = cost + w
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (min_cost[nei], nei))
                elif cost + w == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % mod
            
        return path_count[-1]

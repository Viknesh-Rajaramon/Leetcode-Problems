from typing import List
from heapq import heappop, heappush

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        best_streak, heap = [k+1] * n, [(0, 1, 0)]
        while heap:
            d, streak, u = heappop(heap)
            if streak >= best_streak[u]:
                continue

            best_streak[u] = streak
            if u == n-1:
                return d

            for v, w in graph[u]:
                next_streak = streak + 1 if labels[u] == labels[v] else 1
                if next_streak > k or next_streak >= best_streak[v]:
                    continue

                heappush(heap, (d+w, next_streak, v))

        return -1

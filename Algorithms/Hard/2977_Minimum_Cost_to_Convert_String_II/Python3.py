from typing import List
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for a, b, c in zip(original, cost, changed):
            graph[a].append((b, c))
        
        dfs = defaultdict(lambda: defaultdict(lambda: inf))
        for start in original:
            min_heap, visited = [(0, start)], set()
            while min_heap:
                dist, u = heappop(min_heap)
                if u in visited:
                    continue
                
                visited.add(u)
                dfs[start][u] = dist
                for w, v in graph[u]:
                    if v not in visited:
                        heappush(min_heap, (w + dist, v))
        
        n = len(source)
        dp = [inf] * (n+1)
        dp[0] = 0

        original_set = set(original)
        valid_lengths = set(len(s) for s in original_set)
        for i in range(n):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                if dp[i] < dp[i+1]:
                    dp[i+1] = dp[i]
            
            for l in valid_lengths:
                if i+l > n or source[i : i+l] not in original_set:
                    continue
                
                if dfs[source[i : i+l]][target[i : i+l]] == inf:
                    continue
                
                new = dp[i] + dfs[source[i : i+l]][target[i : i+l]]
                if new < dp[i+l]:
                    dp[i+l] = new

        return -1 if dp[n] == inf else dp[n]

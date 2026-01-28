from typing import List
from collections import defaultdict, deque

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def bfs(start: int) -> List[int]:
            queue, dist = deque([start]), [-1] * n
            dist[start] = 0
            while queue:
                u = queue.popleft()
                for v in tree[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        queue.append(v)
            
            return dist
        
        dx, dy, dz = bfs(x), bfs(y), bfs(z)

        result = 0
        for i in range(n):
            d = sorted([dx[i], dy[i], dz[i]])
            if d[0] != -1 and d[0]*d[0] + d[1]*d[1] == d[2]*d[2]:
                result += 1

        return result

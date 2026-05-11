from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def is_valid(threshold: int) -> bool:
            queue, visited = deque([(source, 0)]), set([(source, 0)])
            while queue:
                u, heavy = queue.popleft()
                if u == target:
                    return True
                
                for v, w in graph[u]:
                    new_h = heavy + (1 if w > threshold else 0)
                    if new_h <= k and (v, new_h) not in visited:
                        visited.add((v, new_h))
                        queue.append((v, new_h))
            
            return False
        
        result, low, high = -1, 0, max([w for _, _, w in edges], default=0)
        while low <= high:
            mid = (low + high)//2
            if is_valid(mid):
                result = mid
                high = mid-1
            else:
                low = mid+1

        return result

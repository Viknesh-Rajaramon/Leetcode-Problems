from imports import *

class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0
        
        dist, max_dist = [[0] * n for _ in range(n)], 0
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = dist[j][i] = d
                if max_dist < d:
                    max_dist = d
        
        def can_partition(pf: int) -> bool:
            color = [-1] * n
            for i in range(n):
                if color[i] != -1:
                    continue
                
                color[i], queue = 0, deque([i])
                while queue:
                    u = queue.popleft()
                    for v in range(n):
                        if u == v:
                            continue
                        
                        if dist[u][v] < pf:
                            if color[v] == -1:
                                color[v] = color[u] ^ 1
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False
                
            return True
        
        low, high = 0, max_dist + 1
        while low < high:
            mid = (low + high + 1) // 2

            if can_partition(mid):
                low = mid
            else:
                high = mid - 1
        
        return low

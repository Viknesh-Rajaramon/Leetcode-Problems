from imports import *

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c+1))
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        for u, v in connections:
            parent[find(v)] = find(u)
        
        grid = defaultdict(list)
        for i in range(1, c+1):
            grid[find(i)].append(i)

        for heap in grid.values():
            heapify(heap)

        result, offline = [], [False] * (c+1)
        for t, x in queries:
            if t == 2:
                offline[x] = True
            else:
                if not offline[x]:
                    result.append(x)
                else:
                    heap = grid[find(x)]
                    while heap and offline[heap[0]]:
                        heappop(heap)
                    
                    result.append(heap[0] if heap else -1)
        
        return result

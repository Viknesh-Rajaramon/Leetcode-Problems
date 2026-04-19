from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        class UF:
            def __init__(self, n: int):
                self.parent = list(range(n+2))
            
            def find(self, x: int) -> int:
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int):
                self.parent[self.find(x)] = self.find(y)
        
        events.sort(key = lambda x: x[1])

        uf = UF(events[-1][1])

        result = 0
        for start, end in events:
            day = uf.find(start)
            
            if day <= end:
                result += 1
                uf.union(day, day+1)

        return result

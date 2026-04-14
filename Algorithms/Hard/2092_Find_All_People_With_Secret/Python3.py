from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        class UnionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.rank = [0] * n
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> None:
                x, y = self.find(x), self.find(y)
                if x != y:
                    if self.rank[x] > self.rank[y]:
                        self.parent[y] = x
                    elif self.rank[x] < self.rank[y]:
                        self.parent[x] = y
                    else:
                        self.parent[y] = x
                        self.rank[x] += 1
            
            def connected(self, x: int, y: int) -> bool:
                return self.find(x) == self.find(y)
            
            def reset(self, x: int) -> None:
                self.parent[x], self.rank[x] = x, 0

        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        uf = UnionFind(n)
        uf.union(0, firstPerson)
        for t in sorted(same_time_meetings.keys()):
            for x, y in same_time_meetings[t]:
                uf.union(x, y)
            
            for x, y in same_time_meetings[t]:
                if not uf.connected(x, 0):
                    uf.reset(x)
                    uf.reset(y)
        
        return [node for node in range(n) if uf.connected(node, 0)]

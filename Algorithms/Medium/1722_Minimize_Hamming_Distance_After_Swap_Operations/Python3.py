from typing import List
from collections import defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y:int) -> None:
                x, y = self.find(x), self.find(y)
                if x != y:
                    self.parent[x] = y
        
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        result = 0
        for key in groups:
            indices, counts = groups[key], defaultdict(int)
            for i in indices:
                counts[source[i]] += 1
            
            for i in indices:
                if counts[target[i]] > 0:
                    counts[target[i]] -= 1
                else:
                    result += 1

        return result

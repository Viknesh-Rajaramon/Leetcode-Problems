from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        class UF:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x) -> int:
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])

                return self.parent[x]

            def union(self, x: int, y: int) -> bool:
                x, y = self.find(x), self.find(y)
                if x != y:
                    if self.rank[x] < self.rank[y]:
                        self.parent[x] = y
                    else:
                        self.parent[y] = x
                        if self.rank[x] == self.rank[y]:
                            self.rank[x] += 1

                    return True
                
                return False

        edges.sort(key = lambda x: x[2], reverse = True)
        components = n

        uf = UF(n)
        for u, v, t in edges:
            if uf.union(u, v):
                components -= 1
                if components < k:
                    return t

        return 0

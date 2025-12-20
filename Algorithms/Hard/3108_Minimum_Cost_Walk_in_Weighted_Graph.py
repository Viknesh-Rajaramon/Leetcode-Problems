from typing import List

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        class UF:
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.size = [1] * n
            
            def find(self, x: int) -> int:
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int):
                x = self.find(x)
                y = self.find(y)

                if x != y:
                    if self.size[x] < self.size[y]:
                        self.parent[x] = y
                        self.size[y] += self.size[x]
                    else:
                        self.parent[y] = x
                        self.size[x] += self.size[y]
        
        uf = UF(n)

        for u, v, w in edges:
            uf.union(u, v)
        
        comp_cost = {}
        for u, v, w in edges:
            root = uf.find(u)
            if root not in comp_cost:
                comp_cost[root] = w
            else:
                comp_cost[root] &= w
        
        ans = []
        for u, v in query:
            r1, r2 = uf.find(u), uf.find(v)

            if r1 != r2:
                ans.append(-1)
            else:
                ans.append(comp_cost[r1])
        
        return ans

from typing import List

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        class UF:
            def __init__(self, n: int) -> None:
                self.parent = list(range(n))
                self.parity = [0] * n
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    px = self.parent[x]
                    self.parent[x] = self.find(px)
                    self.parity[x] ^= self.parity[px]
                
                return self.parent[x]
            
            def union(self, x: int, y: int, w: int) -> bool:
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return (self.parity[x] ^ self.parity[y] ^ w) == 0
                
                self.parent[rx] = ry
                self.parity[rx] = self.parity[x] ^ self.parity[y] ^ w
                return True
        
        uf = UF(n)
        return sum(1 for u, v, w in edges if uf.union(u, v, w))

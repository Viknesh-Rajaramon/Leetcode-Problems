from imports import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UF:
            def __init__(self, n):
                self.parent = list(range(n))
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> bool:
                x, y = self.find(x), self.find(y)
                if x == y:
                    return False

                self.parent[y] = self.parent[x]
                return True
        
        n = len(isConnected)
        uf = UF(n)

        provinces = n
        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1 and uf.union(i, j):
                    provinces -= 1
        
        return provinces

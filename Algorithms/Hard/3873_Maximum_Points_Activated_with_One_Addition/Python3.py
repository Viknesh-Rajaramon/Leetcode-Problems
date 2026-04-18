class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        class UF:
            def __init__(self, n: int) -> None:
                self.parent = list(range(n))
                self.size = [1] * n
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> None:
                x, y = self.find(x), self.find(y)
                if x != y:
                    self.parent[y] = x
                    self.size[x] += self.size[y]
        
        n = len(points)
        uf, x_map, y_map = UF(n), {}, {}
        for i, (x, y) in enumerate(points):
            if x in x_map:
                uf.union(i, x_map[x])
            else:
                x_map[x] = i

            if y in y_map:
                uf.union(i, y_map[y])
            else:
                y_map[y] = i
        
        sizes = sorted([uf.size[i] for i in range(n) if uf.parent[i] == i], reverse = True)
        return sum(sizes[ : 2])+1 if len(sizes) > 1 else sizes[0]+1

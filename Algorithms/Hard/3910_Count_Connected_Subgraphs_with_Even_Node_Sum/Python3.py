class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        class UF:
            def __init__(self, n: int):
                self.parent = list(range(n))
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                
                return self.parent[x]
            
            def union(self, x: int, y: int) -> None:
                self.parent[self.find(x)] = self.parent[self.find(y)]
                return
        
        n = len(nums)
        def is_connected(mask: int, uf: UF) -> bool:
            parent = -1
            for node in [i for i in range(n) if (1 << i) & mask]:
                child = uf.find(node)
                if parent == -1 or child == parent:
                    parent = child
                else:
                    return False
            
            return True
        
        result = 0
        for mask in range(1, 1<<n):
            uf = UF(n)
            for u, v in edges:
                if (1 << u) & mask and (1 << v) & mask:
                    uf.union(u, v)
            
            if sum([nums[i] for i in range(n) if (1<<i)&mask])%2 == 0 and is_connected(mask, uf):
                result += 1

        return result

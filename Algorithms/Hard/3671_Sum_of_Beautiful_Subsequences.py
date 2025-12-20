from typing import List
from collections import defaultdict

class Fenwick:
    def __init__(self, n: int):
        self.tree = [0] * (n+1)
    
    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        
        return s
    
    def add(self, i: int, x: int):
        while i < len(self.tree):
            self.tree[i] += x
            i += i & -i

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        max_ = max(nums) + 1
        
        locs = defaultdict(list)
        for i, num in enumerate(nums):
            locs[num].append(i)
        
        F = [0] * max_
        for d in range(1, max_):
            indices = sorted(i for v in range(d, max_, d) for i in locs[v])
            
            n = len(indices)
            if n <= 1:
                F[d] = n
                continue
            
            rank = {pos: r for r, pos in enumerate(indices, 1)}
            fen = Fenwick(n)
            for v in range(d, max_, d):
                for pos in reversed(locs[v]):
                    r = rank[pos]
                    add = 1 + fen.sum(r-1)
                    F[d] += add
                    fen.add(r, add)
        
        for d in range(max_-1, 0, -1):
            for e in range(2*d, max_, d):
                F[d] -= F[e]
        
            F[d] %= mod
        
        return sum(d * F[d] for d in range(1, max_)) % mod

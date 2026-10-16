from typing import List
from collections import defaultdict

class BIT:
    def __init__(self, n: int):
        self.size = n
        self.tree_1 = defaultdict(int)
        self.tree_2 = defaultdict(int)
    
    def _add(self, idx: int, delta: int) -> None:
        idx += 1
        i = idx
        while idx <= self.size:
            self.tree_1[idx] += delta
            self.tree_2[idx] += (i-1) * delta
            idx += idx & -idx
    
    def add(self, l: int, r: int, delta: int) -> None:
        self._add(l, delta)
        self._add(r+1, -delta)
    
    def _query(self, idx: int) -> int:
        idx += 1
        if idx > self.size:
            idx = self.size
        
        res, i = 0, idx
        while idx > 0:
            res += i * self.tree_1[idx] - self.tree_2[idx]
            idx -= idx & -idx

        return res
    
    def query(self, l: int, r: int) -> int:
        return self._query(r) - self._query(l-1)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result, bit, curr, seen, mod = 0, BIT(len(nums)+10), 0, {}, 10**9+7
        for i, num in enumerate(nums):
            j = seen.get(num, -1)+1
            curr = (curr + bit.query(j, i) * 2 + i - j + 1) % mod
            result = (result + curr) % mod
            bit.add(j, i, 1)
            seen[num] = i

        return result

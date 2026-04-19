from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        class SegmentTree:
            def __init__(self, baskets: List[int]):
                self.n = len(baskets)
                self.seg = [0] * (2 << (self.n - 1).bit_length())
                self._build(baskets, 1, 0, self.n - 1)
            
            def _build(self, a: List[int], v: int, l: int, r: int) -> None:
                if l == r:
                    self.seg[v] = a[l]
                    return
                
                m = (l + r) // 2
                self._build(baskets, v * 2, l, m)
                self._build(baskets, v * 2 + 1, m + 1, r)
                self.seg[v] = max(self.seg[v * 2], self.seg[v * 2 + 1])
            
            def find_and_update(self, v: int, l: int, r: int, x: int) -> int:
                if self.seg[v] < x:
                    return -1
                
                if l == r:
                    self.seg[v] = -1
                    return l
                
                m = (l + r) // 2
                i = self.find_and_update(v * 2, l, m, x)
                if i == -1:
                    i = self.find_and_update(v * 2 + 1, m + 1, r, x)
                
                self.seg[v] = max(self.seg[v * 2], self.seg[v * 2 + 1])
                return i
        
        m = len(baskets)
        if m == 0:
            return len(fruits)
        
        tree = SegmentTree(baskets)
        
        result = 0
        for f in fruits:
            if tree.find_and_update(1, 0, m - 1, f) == -1:
                result += 1

        return result
